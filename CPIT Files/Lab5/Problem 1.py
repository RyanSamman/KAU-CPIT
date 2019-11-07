import math
centerToVertex = eval(input("Enter the length from the center to a vertex: "))

side = 2 * centerToVertex * math.sin(math.pi/5)
area = (3 * math.sqrt(3) / 2) * (side ** 2)

print("the area of the pentagon is", format(area, ".2f"))
