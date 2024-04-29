for value in range(1, 11):
    print(str(value) + "번째 값")

bar = 2.0 + 3 * 4

#1) 2.0 + 3 -> 2.0 + float(3)
#2) 5.0 * 4
#3) 5.0 * float(4)
#4) 20.0




# print(type(2 + 3.0)) # implicit type conersion!! : 2 + 3.0 -> float(2) + 3.0

# #2    + 3.0
# #int  + float -> float
# #float ? (int -> float)

# input_str = input("정수를 입력하세요")
# input_int = int(input_str) # explicit type conversion!!
# #input_str: str -> intrger by using int() function

# print(2 + "3")
