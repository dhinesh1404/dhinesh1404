#Temperature conversion function.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Input temperature in celsius.
celsius = float(input("Enter the temperature in degree celsius: "))

#Convert celsius to fahrenheit.
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print("the fahrenheit temperature is", fahrenheit)
