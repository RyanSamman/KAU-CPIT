
# Imports an accurate value of pi
from math import pi

# Prompts user to assign a value to the radius and length
radius, length = eval(input("Enter the radius and length of a cylinder: "))  # not reliable

# Processes input length and radius into area and volume
area = radius * radius * pi  # value of pi not given, supposed to be 3.14159
volume = area * length

# Displays values of input
print("The area is", area)
print("The volume is", volume)
