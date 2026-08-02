from math import pi
x = float(input("Input the radius of the circle: "))
area = pi * x ** 2
area = round(area, 3)
circumference = 2 * pi * x
circumference = round(circumference, 3)
print(f"Area: {area}\nCircumference: {circumference}")