#Write the program that outputs the following:
#1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19
#using the for statment

for value in range(1, 20):
    if value % 2 != 0:
        print(value, "\t", end= "")
        