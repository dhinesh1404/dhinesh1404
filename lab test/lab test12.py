#Income tax calculation function
def calculate_tax(income):
    if income <= 10000:
        tax = income * 0.10
    
    elif income <= 20000:
        tax = 1000 + (income - 10000) * 0.15
    else:
        tax = 2500 + (income - 20000) * 0.20
    return tax

income = float(input("Enter your income amount: "))

income_tax = calculate_tax(income)
print("Income tax:", income_tax)