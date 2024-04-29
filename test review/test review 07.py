print("-------------------------------")
print("1. Check odd/even program")
print("2. Check multiple of 3 program")
print("-------------------------------")

#selecting a menu.
select_menu = input("Please select a menu options.")

if select_menu =="1":
    print("You have selected the odd-even separator program.")
    int_num = int(input("Please enter an integer value: "))
    if int_num % 2 == 0:
        print(f"The value you entered is {int_num} even")

    else:
        print(f"The value you entered is {int_num} odd")

elif select_menu == "2":
    print("You have selected the multiples of 3 check program.")
    int_num1 = int(input("Please enter an integer value: "))          
    if int_num1 % 3 == 0:
        print(f"The values you entered are multiples of {int_num1}, 3.")
        
    else:
        print(f"The values you entered are not multiples of {int_num1}, 3.")
        
else:
    print(f"The value you entered {select_menu} is an invalid menu selection. Menu selections are only 1 and 2.")
        