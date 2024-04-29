#Write a program that takes 5 positive integer as input and outputs the sum and average.
input_value_1 = int(input("1st value :"))
input_value_2 = int(input("2nd value :"))
input_value_3 = int(input("3rd value :"))
input_value_4 = int(input("4th value :"))
input_value_5 = int(input("5th value :"))


sum = input_value_1 + input_value_2 + input_value_3 + input_value_4 + input_value_5
avg = sum / 5

print("sum:", sum, "\tavg:", avg)





input_num = 5

sum = 0
avg = 0.0

for trial_count in range(1, input_num + 1):
    
    while True:
        msg = str(trial_count) + "Enter the next one :"
        input_value =  int(input(msg))
        
        if input_value > 0:
            break
        sum = sum / input_num
    
avg = sum / input_num

print(sum, avg)