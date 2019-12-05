
def displaySortedNumbers(num1, num2, num3):
    for i in range(3):
        if num1 > num2:
            num2, num1 = num1, num2
        if num2 > num3:
            num3, num2 = num2, num3

    print(num1, num2, num3)


def main():
    input1, input2, input3 = eval(input("Enter three integers: "))
    displaySortedNumbers(input1, input2, input3)


if __name__ == '__main__':
    main()
