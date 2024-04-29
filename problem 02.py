def tringle_type(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "The triangle cannot formed. the sum of the lengths of any two sides is less than or equal to the length of the remaining side: "
    
    if side1 == side2 == side3:
        return "Equilateral triangle"
    
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles triangle"
    
    else:
        return "Scalene triangle"
    
side1 = float(input("Enter the length of side1: "))
side2 = float(input("Enter the length of side2: "))
side3 = float(input("Enter the length of side3: "))
    
result = tringle_type(side1, side2, side3)
print("The tringle type is:", result)       