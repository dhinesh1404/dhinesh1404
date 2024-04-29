# Area converter function: Square meters to square feet
def convert_to_square_feet(square_meters):
    return square_meters * 10.7639

# Area converter function: Square meters to acres
def convert_to_acres(square_meters):
    return square_meters / 4046.86

# Get the user input for land area in square meters
square_meters = float(input("Enter the land area in square meters (m²): "))

# Prompt the user to choose the conversion option
print("Select the conversion:")
print("1. Square Meters to Square Feet")
print("2. Square Meters to Acres")

# Get user choice
choice = int(input("Enter your choice (1 or 2): "))

# Perform the selected conversion and output the result
if choice == 1:
    result = convert_to_square_feet(square_meters)
    print("The land area in square feet is:", result)
elif choice == 2:
    result = convert_to_acres(square_meters)
    print("The land area in acres is:", result)
else:
    print("Invalid choice. Please enter 1 or 2 for the conversion.")
