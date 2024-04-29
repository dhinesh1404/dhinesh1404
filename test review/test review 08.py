#Enter 3 integers and release the biggest emotion.

input_1 = int(input("number 1"))
input_2 = int(input("number 2"))
input_3 = int(input("number 3"))

max = input_1

if max < input_2:
    max = input_2
    
if max < input_3:
    max = input_3
    
print(max)