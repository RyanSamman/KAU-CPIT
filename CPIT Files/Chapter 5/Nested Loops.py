x = 0
y = 0
print("   |  ", end="")
for i in range(1, 10):
    print(format(i, "2.0f"), end="  ")
print("\n----------------------------------------")

while x < 9:
    x += 1
    print(format(x,"2d"), end=" |  ")
    while y < 9:
        y += 1
        print(format(y* x,"2d"), end="  ")
    y = 0
    print()


