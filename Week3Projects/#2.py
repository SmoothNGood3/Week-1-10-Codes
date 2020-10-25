Dependent = 30000.00
Standard = 100000.00
Tax = 0.20
Gross = float(input("What is the gross income: "))
Dependents = int(input("Enter the number of dependents: "))
taxedIncome = Gross - Standard - Dependent * Dependents
incomeTax = taxedIncome * Tax
print("The income tax is " + str(round(incomeTax, 2)))
