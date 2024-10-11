import customtkinter
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
     
def calculate():
    e = equation.get()
    if e != "" and (BisectionSwitch.get() == 1  or NewtonSwitch.get() == 1 or SecantSwitch.get() == 1):
        
        r1.configure(text="Root")
        r2.configure(text="Iterations")
        r3.configure(text="Final Error")
        
        # Bisection method
        if BisectionSwitch.get() == 1:
            c1.configure(text="Bisection method")
            root_bisection, iterations_bisection, error_bisection = bisection_method(e,evaluate_equation, 1, 2, 1e-6, 100)
            br.configure(text=root_bisection)
            bi.configure(text=iterations_bisection)
            bf.configure(text=error_bisection)
        else:
            c1.configure(text="")
            br.configure(text="")
            bi.configure(text="")
            bf.configure(text="")

        # Newton-Raphson method
        if NewtonSwitch.get() == 1:
            c2.configure(text="Newton Raphson method")
            root_newton, iterations_newton, error_newton = newton_raphson_method(e,evaluate_equation, calculate_derivative, 1.5, 1e-6, 100)
            nr.configure(text=root_newton)
            ni.configure(text=iterations_newton)
            nf.configure(text=error_newton)
        else:
            c2.configure(text="")
            nr.configure(text="")
            ni.configure(text="")
            nf.configure(text="")

        # Secant method
        if SecantSwitch.get() == 1:
            c3.configure(text="Secant method")
            root_secant, iterations_secant, error_secant = secant_method(e,evaluate_equation, 1, 2, 1e-6, 100)
            sr.configure(text=root_secant)
            si.configure(text=iterations_secant)
            sf.configure(text=error_secant)
        else:
            c3.configure(text="")
            sr.configure(text="")
            si.configure(text="")
            sf.configure(text="")
            
    else:
        c1.configure(text="")
        c2.configure(text="")
        c3.configure(text="")
        
        r1.configure(text="")
        r2.configure(text="")
        r3.configure(text="")
        
        br.configure(text="")
        bi.configure(text="")
        bf.configure(text="")
        
        nr.configure(text="")
        ni.configure(text="")
        nf.configure(text="")
        
        sr.configure(text="")
        si.configure(text="")
        sf.configure(text="")

if __name__ == '__main__':
    
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")
    
    app = customtkinter.CTk()
    app.geometry("1280x720")
    app.title("CT")
    
    frame = customtkinter.CTkFrame(app)
    frame.pack(pady=20,padx=60,fill="both",expand=True)
    
    topFrame = customtkinter.CTkFrame(frame)
    topFrame.pack(pady=20,padx=60)
    
    equation = customtkinter.CTkEntry(topFrame, placeholder_text="Enter equation",width=500,height=50,font=("Roboto",20))
    equation.grid(row=0,column=0,pady=12,padx=10,columnspan = 2)
    
    cal = customtkinter.CTkButton(topFrame, text="Calculate", command=calculate,width=200,height=40,font=("Roboto",16))
    cal.grid(row=0,column=2,pady=12,padx=10)
    
    BisectionSwitch = customtkinter.CTkSwitch(topFrame,text="Bisection Method",onvalue=1, offvalue=0,font=("Roboto",16))
    BisectionSwitch.grid(row=1,column=0,pady=12,padx=10)
    
    NewtonSwitch = customtkinter.CTkSwitch(topFrame,text="Newton Raphson Method",onvalue=1, offvalue=0,font=("Roboto",16))
    NewtonSwitch.grid(row=1,column=1,pady=12,padx=10)
    
    SecantSwitch = customtkinter.CTkSwitch(topFrame,text="Secant Method",onvalue=1, offvalue=0,font=("Roboto",16))
    SecantSwitch.grid(row=1,column=2,pady=12,padx=10)
    
    bottomFrame = customtkinter.CTkFrame(frame)
    bottomFrame.pack(pady=20,padx=60,fill="both",expand=True)
    
    resultFrame = customtkinter.CTkFrame(bottomFrame,fg_color="transparent")
    resultFrame.pack()
    
    #columns
    c1 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    c1.grid(row=0,column=1,pady=12,padx=10)
    
    c2 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    c2.grid(row=0,column=2,pady=12,padx=10)
    
    c3 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    c3.grid(row=0,column=3,pady=12,padx=10)
    
    #rows
    r1 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    r1.grid(row=1,column=0,pady=12,padx=10)
    
    r2 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    r2.grid(row=2,column=0,pady=12,padx=10)
    
    r3 = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    r3.grid(row=3,column=0,pady=12,padx=10)
    
    #Bisection Method
    br = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    br.grid(row=1,column=1,pady=12,padx=10)
    
    bi = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    bi.grid(row=2,column=1,pady=12,padx=10)
    
    bf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    bf.grid(row=3,column=1,pady=12,padx=10)
    
    #Newton-Raphson Method
    nr = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    nr.grid(row=1,column=2,pady=12,padx=10)
    
    ni = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    ni.grid(row=2,column=2,pady=12,padx=10)
    
    nf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    nf.grid(row=3,column=2,pady=12,padx=10)
    
    #Secant Method
    sr = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    sr.grid(row=1,column=3,pady=12,padx=10)
    
    si = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    si.grid(row=2,column=3,pady=12,padx=10)
    
    sf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    sf.grid(row=3,column=3,pady=12,padx=10)
    
    #message
    message = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    message.grid(row=4,column=0,pady=12,padx=10,columnspan = 4)
    
    app.mainloop()

    # x^3 - x - 2
    # x^3 - 6*x^2 +11*x - 6
    # cos(x) - x
    # e^x - 3*x^2