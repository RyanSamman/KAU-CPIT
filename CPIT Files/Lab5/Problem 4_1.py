inputString = input("Enter an integer: ")
length = len(inputString)

print("The reversed number is", end=" ")
for i in range(1, len(inputString) + 1):
    print(inputString[-i], end="")

