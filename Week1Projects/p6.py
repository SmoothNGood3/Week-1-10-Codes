Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius = int(input("Enter with radius: "))
Enter with radius: 7
>>> area = 3.14*radius**2
>>> print("The area is", area, "square units,")
The area is 153.86 square units,
>>> 
================================================== RESTART: Shell ==================================================
>>> radius = int(input("Enter with radius: "))
Enter with radius: 6.31
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    radius = int(input("Enter with radius: "))
ValueError: invalid literal for int() with base 10: '6.31'
>>> radius = float(input("Enter with radius: "))
Enter with radius: 6.31
>>> area = 3.14*radius**2
>>> print("The area is", area, "square units,")
The area is 125.02255399999999 square units,
>>> 
================================================== RESTART: Shell ==================================================
>>> radius = int(input("Enter with radius: "))
Enter with radius: 14.96
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    radius = int(input("Enter with radius: "))
ValueError: invalid literal for int() with base 10: '14.96'
>>> radius = float(input("Enter with radius: "))
Enter with radius: 14.96
>>> area = 3.14*radius**2
>>> print("The area is", area, "square units,")
The area is 702.7370240000001 square units,
>>> 