a = int(input("What length is on the a side: "))
b = int(input("What length is on the b side: "))
c = int(input("What length is on the c side: "))
if a == b and a == c and b == c:
    print("The triangle is equilateral")
else: 
    print("The triangle is not equilateral")
