#Declare a global variable and get input from the user.
basevalue = float(input("Enter the default value: "))

#Function to perform addition
def add(num):
    global basevalue
    basevalue += num
    
#Function to perform subtraction
def subtract(num):
    global basevalue
    basevalue -= num
    
#Function to perform multiplication
def multiply(num):
    global basevalue
    basevalue *= num
    
#Function to perform division
def division(num):
    global basevalue
    if num == 0:
        print("Error: cannot divide by 0")
    else:
        basevalue /= num

#Selectoperation function
def selectoperation():
    global basevalue
    print("operation result: ", basevalue)
    print("selectoperation: ")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")
    

operation = int(input("Enter opertion number: "))
num = float(input("Enter a number: "))

if operation == 1:
    add(num)
elif operation ==2:
    subtract(num)
elif operation ==3:
    multiply(num)
elif operation ==4:
    division(num)
else:
    print("Invalid operation")
    
selectoperation()