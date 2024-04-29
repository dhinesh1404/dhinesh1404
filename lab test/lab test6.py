#Age is input from the user.
age = int(input("Enter the age: ")) 

#The entered age, users are classifieed as "Teenager." "Adult," or "Senior."
if 13<= age <=19:
    print("You are in the 'Teenager' age group.")

#"Adult" for those between 20 and 64 year old"
elif 20<= age <=64:
    print("You are in the 'Adult' age group.")

#"Senior" for those over 65 years old
elif 65<= age:
    print("You are in the 'Senior' age group.")
                  
#For input value that do not fit the range, "Unknown age group" is output.
else:
    print("You are in the 'Unknown age group' age group.")