#Area converter function.
def convert_to_square_feet(square_meters):
    return(square_meters * 10.7639)

#Input area in acers.
def convert_to_acers(square_meters):
    return(square_meters / 4046.86)

#Get the user input.
square_meters = float(input("Enter the land area in square meters (m²): "))

square_feet = convert_to_square_feet(square_meters)
acers = convert_to_acers(square_meters)

print("Area in square meters: ", square_feet, "ft²" )
print("Area in acers: ", acers, "ac" )