def isValid(side1, side2, side3):
    return side2 + side3 > side1 and side1 + side3 > side2 and side1 + side2 > side3


def area(side1, side2, side3):
    p = (side1 + side2 + side3)/2
    area = (p*(p-side1)*(p-side2)*(p-side3))**0.5
    return area


def main():
    side1, side2, side3 = eval(input("Enter three sides in double: "))

    if isValid(side1, side2, side3):
        print("The area of the triangle is", area(side1, side2, side3))
    else:
        print("Input is invalid")


if __name__ == '__main__':
    main()
