#Receives three integers from the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

#If all numbers are equal, "all numbers are equal",
if num1 == num2 == num3:
    print("all numbers are equal")
    
#If all numbers are differnt.
elif num1 != num2 and num2 != num3 and num3 != num1:
    #find the largest number.
    largest = num1
    if num2 > largest:
        largest = num2
        
    if num3 > largest:
        largest = num3
    print("All the numbers are different, The largest numbers is", largest)

#If the two numbers are same.
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("The two numbers are equal.")
    