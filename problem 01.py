def determines_library_pass(age):
    if age < 12:
        return "Children's pass"
    elif 13 <= age <= 13:
        return "Youth pass"
    else:
        return "Adult ticket"

for _ in range(3):
    age  = int(input("Please enter your's age: "))
    library_pass = determines_library_pass(age)
    print(library_pass, "is available")
    