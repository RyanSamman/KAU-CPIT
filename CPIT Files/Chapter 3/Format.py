from math import sqrt
x1 = 5
x2 = 500
x3 = 20
x4 = 3000
List = [x1, x2, x3, x4]

print("-------------------------------")
print(format("x", ">6s") + "| " + format("x^2", "13s") + format("√x", "s"))
# print("     x| x^2          √x        ")
print("-------------------------------")

for i in List:
    print(format(i, "6.0f") + "| " + format(i**2, "<13.2f") + format(sqrt(i), ".2f"))

print("-------------------------------")
# print(format(5, "6.0f") + "| " + format(25, "<13.2f") + format(2.24, ".2f"))

