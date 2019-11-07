from random import randint

number1 = randint(0, 9)
number2 = randint(0, 9)

answer = number1 + number2

string = str(number1) + " + " + str(number2)
inputNo = eval(input("What is " + string + ": "))
state = (inputNo == answer)

print(string,"=", inputNo, "is", state)