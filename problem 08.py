#Receives a natural numbers N as a input
N = int(input("Enter a natural number N: "))

#Increase the number of stars by 1 from the first row to the Nth row.
for i in range(1, N, +1):
    print("*" * i)
    
#Decreased the star from the Nth row to last line.
for i in range(N -1, 0, -1):
    print("*" * i)
    