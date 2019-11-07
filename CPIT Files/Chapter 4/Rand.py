import random
# if file name is random it won't work cuz its ***

x = random.randint(0, 9)  # Generates a number between 0 and 9 inclusive
print(x)

y = random.randrange(0, 10)  # Generates an integer between 0 and up to but not including 10
print(y)

z = round((random.random() * (10 ** 4)), 2)  # 4 digits before . 2 after
print(z)

a, b = 1, 3
number = a + (random.random() * (b - a))
print(number)