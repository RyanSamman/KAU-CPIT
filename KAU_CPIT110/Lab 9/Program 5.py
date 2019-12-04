from random import randint


def printMatrix(n):
    outstring = ""
    for i in range(n):
        for j in range(n):
            outstring += str(randint(0, 1))
            outstring += " "
        outstring += "\n"
    print(outstring)


def main():
    n = eval(input("Enter n: "))
    printMatrix(n)


if __name__ == '__main__':
    main()
