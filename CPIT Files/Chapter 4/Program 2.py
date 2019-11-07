inputNumber = eval(input("Enter an integer: "))

remainder5 = inputNumber % 5
remainder2 = inputNumber % 2
# If 0 is inputted, it will display HiFive and HiEven so we filter it through an if

if inputNumber == 0:
    print("Input number is 0, HiFive and HiEven")
else:
    if remainder2 == 0:
        print("HiEven")
    if remainder5 == 0:
        print("HiFive")
    else:
        print("Error")

