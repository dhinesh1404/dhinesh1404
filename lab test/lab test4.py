#Receives distance input on kilometers from the user.
distance = int(input("Enter the distance to travel in kilometers: "))

#Speed of light per second.
speed = 299792

#The time to travel a distance at the speed.
time = distance/speed

print("The time it takes light to travel",float(distance), "kilometers is", time, "Seconds")