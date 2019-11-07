integer1 = eval(input("Enter first integer: "))
integer2 = eval(input("Enter second integer: "))

commonDivisors = [0]

for i in range(1, integer1):
    if (integer1 % i == 0) and (integer2 % i == 0):
        commonDivisors += [i]


greatestCommonDivisor = max(commonDivisors)
print(greatestCommonDivisor)