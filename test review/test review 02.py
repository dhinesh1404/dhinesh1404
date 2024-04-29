while True:
    #Enter menu
    print("-" * 10)
    print("1, the output of the mulitiplication table")
    print("2, end the program")
    print("-" * 10)
    
    #enter menu values
    selected_menu = input("Enter the menu value :")
    
    #menu value == 1
    if selected_menu == "1":
        dan = int(input("Please enter the dan: "))
        
        if 2 <= dan <= 9:
            for num in range(1, 10):
                print(dan, "x", num, "-", dan * num)
            break
        print("Enter an integer value between 2 and 9")
        
        





