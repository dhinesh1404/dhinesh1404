#If 0 is input, "0" is output and "Positive integer" is ouput if it  exceeds 0. If it is less than 0, "negetive integer" is output.

input_value = int(input("정수 입력: "))

if input_value == 0:
    print("0")
elif input_value > 0:
    print("positive integer")
else:
    print("negetive integer")
    
