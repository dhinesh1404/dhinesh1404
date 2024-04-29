#Receive one character input from the user.
bar = input("Please enter one character: ")

#Check whether the entered character is a vowel or not.
if bar.lower() in ['a','e','i','o','u']:
    print(bar, "is a lower: ")
else:
    print(bar, "is not a lower: ")
