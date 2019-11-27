
def displaySortedNumbers(num1, num2, num3):    
    for i in range(2):
        if num2 > num1:
            num1, num2 = num2, num1
        if num3 > num2:
            num3, num2 = num2, num3
        
    print(num1, num2, num3)


def main():
    num1, num2, num3 = eval(input("Enter three integers: "))
    displaySortedNumbers(num1, num2, num3)


if __name__ == '__main__':
    main()