from math import pi

radius = eval(input("Enter a radius: "))

if radius >= 0:
    area = (radius ** 2) * pi
    print("the area is", area)
else:
    print("invalid input")
