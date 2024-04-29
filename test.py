input_number = "990414 - 5180045"
check_number = [2,3,4,5,6,7,8,9,2,3,4,5,]


#Check validation

#After mulitiplying 12 digits of the resident number by the check value for each digit
#Resident number 12 digits : 0 index -> 11 index
sum = 0
count = 0
for num in input_number:
    if num != "-" and count < 12:
       sum += int(num) * check_number[count]
       count += 1
       
check_value = (11 - (sum % 11)) % 10

if check_value == int(input_number[-1]):
    print("Valid resident number")
else:
    print("Invalid resident number")