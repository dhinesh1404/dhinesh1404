menus = ["Pizza", "Pasta", "salad", "Sushi", "Burger"]

#Receive the index from the user.
index = (input("Select the index of the menu(starting from 0): "))

#Check if index is valid.
index = int(index)
if index > len(menus):
    print("Invalid selection.")
else:
    print("Your selection menus:", menus[index])
    

