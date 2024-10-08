import math
import sympy as sp

# Bisection Method
def bisection_method(e,f, a, b, tol, max_iter):
    #if f(a) * f(b) > 0:
    #    raise ValueError("The function must have opposite signs at the interval boundaries.")
    
    iters = 0
    while iters < max_iter:
        c = (a + b) / 2.0
        if abs(f(e,c)) < tol or (b - a) / 2.0 < tol:
            return c, iters, abs(f(e,c))
        
        iters += 1
        if f(e,c) * f(e,a) < 0:
            b = c
        else:
            a = c

    return c, iters, abs(f(e,c))

# Newton-Raphson Method
def newton_raphson_method(e,f, f_prime, x0, tol, max_iter):
    x = x0
    iters = 0
    while iters < max_iter:
        f_x = f(e,x)
        f_prime_x = f_prime(e,x)
        
        if abs(f_x) < tol:
            return x, iters, abs(f_x)
        
        if f_prime_x == 0:
            raise ValueError("Zero derivative encountered; the method cannot proceed.")
        
        x_new = x - f_x / f_prime_x
        if abs(x_new - x) < tol:
            return x_new, iters, abs(x_new - x)
        
        x = x_new
        iters += 1

    return x, iters, abs(f(e,x))

# Secant Method
def secant_method(e,f, x0, x1, tol, max_iter):
    iters = 0
    while iters < max_iter:
        f_x0 = f(e,x0)
        f_x1 = f(e,x1)
        
        if abs(f_x1) < tol:
            return x1, iters, abs(f_x1)
        
        if f_x1 - f_x0 == 0:
            raise ValueError("Zero division encountered; the method cannot proceed.")
        
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x_new - x1) < tol:
            return x_new, iters, abs(x_new - x1)
        
        x0 = x1
        x1 = x_new
        iters += 1

    return x1, iters, abs(f(e,x1))
        
def evaluate_equation(equation, x):
    equation = equation.replace('e^x','math.exp(x)')
    equation = equation.replace('X','x').replace(" ","").replace("^","**")
    equation = equation.replace('cos(x)','math.cos(x)').replace('sin(x)','math.sin(x)').replace('tan(x)','math.tan(x)')
    return eval(equation.replace('x', str(x)))

def calculate_derivative(equation,a):
    equation = equation.replace('X','x').replace(" ","").replace("^","**")
    x = sp.symbols('x')
    sympy_eq = sp.sympify(equation)
    derivative = sp.diff(sympy_eq, x)
    return evaluate_equation(str(derivative),a)

def main():
    equation = input("Enter equation: ")
    #Bisection method example
    root_bisection, iterations_bisection, error_bisection = bisection_method(equation,evaluate_equation, 1, 2, 1e-6, 100)
    print("Bisection Method:")
    print(f"Root: {root_bisection}, Iterations: {iterations_bisection}, Final Error: {error_bisection}\n")

    # Newton-Raphson method example
    root_newton, iterations_newton, error_newton = newton_raphson_method(equation,evaluate_equation, calculate_derivative, 1.5, 1e-6, 100)
    print("Newton-Raphson Method:")
    print(f"Root: {root_newton}, Iterations: {iterations_newton}, Final Error: {error_newton}\n")

    # Secant method example
    root_secant, iterations_secant, error_secant = secant_method(equation,evaluate_equation, 1, 2, 1e-6, 100)
    print("Secant Method:")
    print(f"Root: {root_secant}, Iterations: {iterations_secant}, Final Error: {error_secant}")

if __name__ == '__main__':
    main()

    # x^3 - x - 2
    # x^3 - 6*x^2 +11*x - 6
    # cos(x) - x
    # e^x - 3*x^2