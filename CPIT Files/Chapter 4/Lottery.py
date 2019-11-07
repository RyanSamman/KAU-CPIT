import random

lotteryNumber = random.randint(0, 99)
print("The lottery number is", lotteryNumber)
lotteryGuess = eval(input("Enter your lottery pick (two digits): "))

# Ex. 45 lotteryNumber1 is 4 and lotteryNumber2 is 5
lotteryNumber1 = lotteryNumber // 10
lotteryNumber2 = lotteryNumber % 10

lotteryGuess1 = lotteryGuess // 10
lotteryGuess2 = lotteryGuess % 10


if lotteryNumber == lotteryGuess:
    print("Match on same order: you win $10,000")
elif (lotteryNumber1 == lotteryGuess2) and (lotteryNumber2 == lotteryGuess1):
    print("Match but not in same order: you win $3,000")
elif (lotteryNumber1 == lotteryGuess1
        or lotteryNumber2 == lotteryGuess2
        or lotteryNumber2 == lotteryGuess1
        or lotteryNumber1 == lotteryGuess2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")






































































































