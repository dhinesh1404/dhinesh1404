#If the input value is odd and is a multiple of 3, print it out.

input_value = int(input("정수 값 입력:"))

if input_value % 2 == 1:
    if input_value % 3 == 0:
        print(input_value)
        
if input_value % 2 == 1 and input_value % 3 == 0:
    print(input_value)