#Enter two mistakes using the keyboard.
num1 = input("Enter the first number :")
num2 = input("Enter the secound number :")

#Select an operator.
operator = input("Select an operator(enter one of +, -, *, /) :")

#Enter one of the data type.
data_type = input("Result value data type(enter one of integer, float,or string) :")


#make calculate variables
add = float(num1) + float(num2)
sub = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)
#chose an operator.
if data_type == "integer":
    if operator == "+":
        print(f"{num1} + {num2} = {int(add)} ")
    elif operator == "-":
        print(f"{num1} - {num2} = {int(sub)} ")
    elif operator == "*":
        print(f"{num1} * {num2} = {int(multiply)} ")
    elif operator == "/":
        print(f"{num1} / {num2} = {int(divide)} ")
        
    elif data_type == "float":
        if operator == "+":
            print(f"{num1} + {num2} = {float(add)} ")
        elif operator == "-":
            print(f"{num1} - {num2} = {float(sub)} ")
        elif operator == "*":
            print(f"{num1} * {num2} = {float(multiply)} ")
        elif operator == "/":
            print(f"{num1} / {num2} = {float(divide)} ")
            
    elif data_type == "string":
        if operator == "+":
            print(f"{num1} + {num2} = {str(add)} ")
        elif operator == "-":
            print(f"{num1} - {num2} = {str(sub)} ")
        elif operator == "*":
            print(f"{num1} * {num2} = {str(multiply)} ")
        elif operator == "/":
            print(f"{num1} / {num2} = {str(divide)} ")

        
        
            
     
