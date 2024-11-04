import customtkinter # Import customtkinter for creating GUI interface
import math # Import math for mathematical operations
import sympy as sp # Import sympy for symbolic mathematics, particularly for calculating derivatives

equation=""

# Bisection Method
def bisection_method(f, a, b, tol, max_iter):
    iters = 0
    
    # Check if initial endpoints are roots
    if f(a) == 0:
        setValues([message],[f"{a} value is already root value"])
        return a, 1, 0
    elif f(b) == 0:
        setValues([message],[f"{b} value is already root value"])
        return b, 1, 0
    
    while iters < max_iter:
        
        c = (a + b) / 2.0 # Calculate midpoint
        
        # Check if midpoint is root or tolerance is met
        if f(c) == 0 or abs(b - a)/2.0 < tol:
            return c, iters, abs(b - a)/2.0
        elif f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        elif f(a) * f(b) >= 0:
            a += 1
            b -= 1
            
        iters += 1

    return c, iters, abs(b - a)/2.0

# Newton-Raphson Method
def newton_raphson_method(f, f_prime, x0, tol, max_iter):
    x = x0
    iters = 0
    while iters < max_iter:
        f_x = f(x)
        f_prime_x = f_prime(x)
        
        # Check if function value is within tolerance
        if abs(f_x) < tol:
            return x, iters, abs(x0 - x)
        
        # Check if derivative is zero to avoid division by zero
        if f_prime_x == 0:
            setValues([message],["Zero derivative encountered"])
            return x, iters, abs(x0 - x)
        
        # Update value using Newton-Raphson formula
        x_new = x - f_x / f_prime_x
        
        if abs(x_new - x) < tol:
            return x_new, iters, abs(x - x_new)
        
        x0 = x
        x = x_new
        iters += 1

    return x, iters, abs(x0 - x)

# Secant Method
def secant_method(f, x0, x1, tol, max_iter):
    iters = 0
    while iters < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Check if function value is within tolerance
        if abs(f_x1) < tol:
            return x1, iters, abs(x0 - x1)
        
         # Check if difference is zero to avoid division by zero
        if f_x1 - f_x0 == 0:
            setValues([message],["Zero division encountered"])
            return x1, iters, abs(x0 - x1)
        
        # Update value using Secant formula
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x_new - x1) < tol:
            return x_new, iters, abs(x1 - x_new)
        
        x0 = x1
        x1 = x_new
        iters += 1

    return x1, iters, abs(x0 - x1)
        
# Function to evaluate the given equation at a specific value of x.
def evaluate_equation(x):
    e = equation
    e = e.replace('cos(x)','math.cos(x)').replace('sin(x)','math.sin(x)').replace('tan(x)','math.tan(x)').replace('exp(x)','math.exp(x)')
    return eval(e)

# Function to calculate the derivative of the given equation using sympy and evaluate it at a specific value of x.
def calculate_derivative(x):
    e = equation
    X = sp.symbols('x')
    sympy_eq = sp.sympify(e)
    derivative = sp.diff(sympy_eq, X)
    e = str(derivative)
    e = e.replace('cos(x)','math.cos(x)').replace('sin(x)','math.sin(x)').replace('tan(x)','math.tan(x)').replace('exp(x)','math.exp(x)')
    return eval(e)

# Function to process the user input equation to make it suitable for evaluation.
def get_equation(e):
    e = e.replace('e^x','exp(x)')
    e = e.replace('X','x').replace(" ","").replace("^","**")
    global equation
    equation = e
    return e

# Function to extract the initial guesses or interval endpoints from the user input.
def get_guess(n):
    if n.find(",") == -1:
        return float(n),0
    else:
        a,b =  n.split(",")
        return float(a),float(b)
    
# Function to clear the text values for the specified GUI elements.
def clearValues(variables):
    for variable in variables:
        variable.configure(text="")
       
# Function to set the specified values for the given GUI elements. 
def setValues(variables,values):
    i=0
    while i<len(variables):
        variables[i].configure(text=values[i])
        i += 1
    
# Function to handle errors and validate the user input before performing calculations.
def error_handling(equation,iteration,toleranc,guess,Bisection,Newton,Secant):
    
    # Prompt user to enter an equation if empty
    if equation == "":
        setValues([message],["Enter Equation"])
        return False
    
    # Prompt user to enter maximum iteration value if empty
    if iteration == "":
        setValues([message],["Enter Max Iteration value"])
        return False
    
    # Prompt user to enter tolerance value if empty
    if toleranc == "":
        setValues([message],["Enter Toleranc value"])
        return False
    
     # Prompt user to enter initial guess values if empty
    if guess == "":
        setValues([message],["Enter interval or initial guess values"])
        return False
    
    # Prompt user to select at least one method if none selected
    if Bisection == 0 and Newton == 0 and Secant == 0:
        setValues([message],["Select at least one of methods"])
        return False
        
    clearValues([message])
    return True
     
# Function to calculate the root of the equation based on the selected method(s) and display the results.
def calculate():
    
    equation = equationTextField.get()
    iteration = iterationTextField.get()
    toleranc = toleranceTextField.get()
    guess = guessTextField.get()
    Bisection = BisectionSwitch.get()
    Newton = NewtonSwitch.get()
    Secant = SecantSwitch.get()
    
    if error_handling(equation,iteration,toleranc,guess,Bisection,Newton,Secant):
        
        equation = get_equation(equation)
        iteration = float(iteration)
        toleranc = float(toleranc)
        a,b = get_guess(guess)
        
        setValues([r1,r2,r3],["Root","Iterations","Final Error"])
        
        # Bisection method
        if Bisection == 1:
            setValues([c1],["Bisection method"])
            bisectionResult = bisection_method(evaluate_equation, a, b, toleranc, iteration)
            setValues([br,bi,bf],bisectionResult)
        else:
            clearValues([c1,br,bi,bf])

        # Newton-Raphson method
        if Newton == 1:
            setValues([c2],["Newton Raphson method"])
            newtonResult = newton_raphson_method(evaluate_equation, calculate_derivative, a, toleranc, iteration)
            setValues([nr,ni,nf],newtonResult)
        else:
            clearValues([c2,nr,ni,nf])

        # Secant method
        if Secant == 1:
            setValues([c3],["Secant method"])
            secantResult = secant_method(evaluate_equation, a, b, toleranc, iteration)
            setValues([sr,si,sf],secantResult)
        else:
            clearValues([c3,sr,si,sf])
            
    else:
        clearValues([c1,c2,c3,r1,r2,r3,br,bi,bf,nr,ni,nf,sr,si,sf])

if __name__ == '__main__':
    # Set appearance mode and color theme for the GUI
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")
    
    # Create main application window
    app = customtkinter.CTk()
    app.geometry("1280x720")
    app.title("CT")
    
    # Create main frame
    frame = customtkinter.CTkFrame(app)
    frame.pack(pady=20,padx=60,fill="both",expand=True)
    
    # Create top frame for user inputs
    topFrame = customtkinter.CTkFrame(frame)
    topFrame.pack(pady=20,padx=60)
    
    # Create entry fields and button for user inputs
    equationTextField = customtkinter.CTkEntry(topFrame, placeholder_text="Enter equation",width=500,height=50,font=("Roboto",20))
    equationTextField.grid(row=0,column=0,pady=12,padx=10,columnspan = 2)
    
    cal = customtkinter.CTkButton(topFrame, text="Calculate", command=calculate,width=200,height=50,font=("Roboto",16))
    cal.grid(row=0,column=2,pady=12,padx=10,sticky="e")
    
    iterationTextField = customtkinter.CTkEntry(topFrame, placeholder_text="Enter Max Iteration",width=240,height=50,font=("Roboto",20))
    iterationTextField.grid(row=1,column=0,pady=12,padx=10,sticky="w")
    
    toleranceTextField = customtkinter.CTkEntry(topFrame, placeholder_text="Enter Tolerance",width=240,height=50,font=("Roboto",20))
    toleranceTextField.grid(row=1,column=1,pady=12,padx=10,sticky="e")
    
    guessTextField = customtkinter.CTkEntry(topFrame, placeholder_text="Enter  interval/Guess",width=200,height=50,font=("Roboto",20))
    guessTextField.grid(row=1,column=2,pady=12,padx=10,sticky="w")
    
    # Create switches for selecting methods
    BisectionSwitch = customtkinter.CTkSwitch(topFrame,text="Bisection Method",onvalue=1, offvalue=0,font=("Roboto",16))
    BisectionSwitch.grid(row=2,column=0,pady=12,padx=10)
    
    NewtonSwitch = customtkinter.CTkSwitch(topFrame,text="Newton Raphson Method",onvalue=1, offvalue=0,font=("Roboto",16))
    NewtonSwitch.grid(row=2,column=1,pady=12,padx=10)
    
    SecantSwitch = customtkinter.CTkSwitch(topFrame,text="Secant Method",onvalue=1, offvalue=0,font=("Roboto",16))
    SecantSwitch.grid(row=2,column=2,pady=12,padx=10)
    
    # Create bottom frame for displaying results
    bottomFrame = customtkinter.CTkFrame(frame)
    bottomFrame.pack(pady=20,padx=60,fill="both",expand=True)
    
    resultFrame = customtkinter.CTkFrame(bottomFrame,fg_color="transparent")
    resultFrame.pack()
    
    # Create labels for displaying results
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
    
    #Bisection Method results
    br = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    br.grid(row=1,column=1,pady=12,padx=10)
    
    bi = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    bi.grid(row=2,column=1,pady=12,padx=10)
    
    bf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    bf.grid(row=3,column=1,pady=12,padx=10)
    
    #Newton-Raphson Method  results
    nr = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    nr.grid(row=1,column=2,pady=12,padx=10)
    
    ni = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    ni.grid(row=2,column=2,pady=12,padx=10)
    
    nf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    nf.grid(row=3,column=2,pady=12,padx=10)
    
    #Secant Method  results
    sr = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    sr.grid(row=1,column=3,pady=12,padx=10)
    
    si = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    si.grid(row=2,column=3,pady=12,padx=10)
    
    sf = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",font=("Roboto",24),justify="left")
    sf.grid(row=3,column=3,pady=12,padx=10)
    
    # Message label for feedback or errors
    message = customtkinter.CTkLabel(resultFrame, text="", fg_color="transparent",text_color="#D0342C",font=("Roboto",24),justify="left")
    message.grid(row=4,column=0,pady=12,padx=10,columnspan = 4)
    
    # Start the main loop of the application
    app.mainloop()

    # Test equations
    # x^3 - x - 2
    # x^3 - 6*x^2 +11*x - 6
    # cos(x) - x
    # e^x - 3*x^2