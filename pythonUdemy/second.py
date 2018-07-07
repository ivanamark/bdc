# Write a program to calculate the diameter, circumference, and the area of circle using the value of radius and constant PI = 3.14159.
radius=input("Please enter your radius: ")
PI = 3.14159
diameter=2*radius
circumference=float(diameter)*PI
area=(float(radius)**2) * PI
print(area)
print(diameter)
print(circumference)
print(type(area))