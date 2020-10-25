wage = float(input("How much do we pay the employee: "))
hours = int(input("How many hours did he work: "))
ot = int(input("How much overtime did he work: "))
overtime = ot * (wage*1.5)
equation = (wage * hours) + overtime
print("The worker will end up making", equation)
