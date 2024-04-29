#Among the integers between 11 and 30,print the number of blank numbers.


for count in range(1,31):
    if count % 2 == 0 and count % 5 == 0:
        print(count, "\t", end="")