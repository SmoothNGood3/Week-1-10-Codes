from math import sqrt

A = int(input("What is the length for side A?: "))
B = int(input("What is the length for side B?: "))
C = int(input("What is the length for side C?: "))

if C == sqrt(A * A + B * B):
	print('The triangle is a right triangle with C as the hypotenuse.')

elif B == sqrt(A * A + C * C):
	print('The triangle is a right triangle with B as the hypotenuse.')

elif A == sqrt(C * C + B * B):
	print('The triangle is a right triangle with A as the hypotenuse.')

else:
    print('The triangle is not a right triangle.')
