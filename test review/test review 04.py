#Among the integers between 1 and 100, print the multiples of 3 and 7.

for value in range(1,101):
    if value % 3 == 0 or value % 7 == 0:
        print(value,"\t", end= "")
        
        