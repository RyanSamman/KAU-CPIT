import time
import random
i = 0
correct = 0
continueLoop = "Y"
timeTaken = time.time()

while continueLoop == "Y":
    i += 1
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    if number2 >= number1:
        number1, number2 = number2, number1

    number3 = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

    if number3 == (number1 - number2):
        print("You are correct!")
        correct += 1
    else:
        print("Your answer is wrong.")
        print(number1, "-", number2, "is", number1 - number2)
    continueLoop = input("Enter Y to continue and N to quit: ")

timeTaken = int(time.time() - timeTaken)
print("\nCorrect count is", correct, "out of", i)
print("Test time is", timeTaken, "seconds")

