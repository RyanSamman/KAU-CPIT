import random

winCount = count = 0

print("Type \"Exit\" to Exit and \"Reset\" to reset score")
handPlayer = input("Input Rock, Paper, Scissors: ")

N2A = ["Scissors", "Rock", "Paper"]

# 1 = win
# 0 = draw
# -1 = loss


def win(i1, i2):
    if i1 == "Rock":
        if i2 == "Paper":
            return -1
        if i2 == i1:
            return 0
        else:
            return 1
    elif i1 == "Paper":
        if i2 == "Scissors":
            return -1
        if i2 == i1:
            return 0
        else:
            return 1
    elif i1 == "Scissors":
        if i2 == "Paper":
            return -1
        if i2 == i1:
            return 0
        else:
            return 1
    else:
        print("Error! input is wrong")


while handPlayer != "Exit":
    if handPlayer == "Reset":
        winCount = count = 0
        clear()
        print("Type \"Exit\" to Exit and \"Reset\" to reset score")

    else:
        count += 1
        handComputer = N2A[random.randrange(0, 3)]
        state = win(handPlayer, handComputer)

        if state == 1:
            print("\nWin!", handPlayer, "beats", handComputer)
            winCount += 1
            print(winCount, "Wins out of", count)

        elif state == 0:
            print("\nDraw.", handPlayer, "is against", handComputer)
            print(winCount, "Wins out of", count)

        elif state == -1:
            print("\nLoss!", handComputer, "beats", handPlayer)
            print(winCount, "Wins out of", count)

        else:
            print("\nError!")
            count -= 1
            print(winCount, "Wins out of", count)

    print(winCount, "Wins out of", count)
    handPlayer = input("\nInput Rock, Paper, Scissors: ")
