import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number2 >= number1:
    number1, number2 = number2, number1

number3 = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

if number3 == (number1 - number2):
    print("You are correct!")
else:
    print("Your answer is wrong.\n",
          number1, "-", number2, "is", number1-number2)
