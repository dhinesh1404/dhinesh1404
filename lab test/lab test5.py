#Receive string input of "man" or "woman" from the user.
gender = input("Please enter your gender (man/woman): ")

#If it's a "man", convert it to "MAN"
if gender == "man":
    print("MAN")

#If it's a "woman", convert it to "WOMAN" 
elif gender == "woman":
    print("WOMAN")

#If not both "Invalid input".
else:
    print("Invalid input: ")