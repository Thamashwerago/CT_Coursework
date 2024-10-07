# Bisection Method
def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) > 0:
        raise ValueError("The function must have opposite signs at the interval boundaries.")
    
    iters = 0
    while iters < max_iter:
        c = (a + b) / 2.0
        if abs(f(c)) < tol or (b - a) / 2.0 < tol:
            return c, iters, abs(f(c))
        
        iters += 1
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, iters, abs(f(c))

# Newton-Raphson Method
def newton_raphson_method(f, f_prime, x0, tol, max_iter):
    x = x0
    iters = 0
    while iters < max_iter:
        f_x = f(x)
        f_prime_x = f_prime(x)
        
        if abs(f_x) < tol:
            return x, iters, abs(f_x)
        
        if f_prime_x == 0:
            raise ValueError("Zero derivative encountered; the method cannot proceed.")
        
        x_new = x - f_x / f_prime_x
        if abs(x_new - x) < tol:
            return x_new, iters, abs(x_new - x)
        
        x = x_new
        iters += 1

    return x, iters, abs(f(x))

# Secant Method
def secant_method(f, x0, x1, tol, max_iter):
    iters = 0
    while iters < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
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

    return x1, iters, abs(f(x1))

# Define a test function and its derivative for Newton-Raphson
def f(x):
    return x**3 - x - 2

def f_prime(x):
    return 3*(x**2) - 1

def main():
    #Bisection method example
    root_bisection, iterations_bisection, error_bisection = bisection_method(f, 1, 2, 1e-6, 100)
    print("Bisection Method:")
    print(f"Root: {root_bisection}, Iterations: {iterations_bisection}, Final Error: {error_bisection}\n")

    # Newton-Raphson method example
    root_newton, iterations_newton, error_newton = newton_raphson_method(f, f_prime, 1.5, 1e-6, 100)
    print("Newton-Raphson Method:")
    print(f"Root: {root_newton}, Iterations: {iterations_newton}, Final Error: {error_newton}\n")

    # Secant method example
    root_secant, iterations_secant, error_secant = secant_method(f, 1, 2, 1e-6, 100)
    print("Secant Method:")
    print(f"Root: {root_secant}, Iterations: {iterations_secant}, Final Error: {error_secant}")

if __name__ == '__main__':
    main()