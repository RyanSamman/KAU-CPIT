def displaySortedNumbers1(args):
    count = 0
    while count < len(args) ** 2:
        for i in range(len(args) - 1):
            if eval(args[i + 1]) < eval(args[i]):
                args[i+1], args[i] = args[i], args[i+1]
        count += 1
    return args


def displaySortedNumbers2(args):
    count = 0
    while count < len(args) ** 2:
        for i in range(len(args) - 1):
            if eval(args[i + 1]) > eval(args[i]):
                args[i], args[i+1] = args[i + 1], args[i]
        count += 1
    return args


def main():
    in_string = input("Enter numbers to be sorted: ")
    in_string = in_string.split(", ")

    sorted_numbers = displaySortedNumbers1(in_string)

    #print(sorted_numbers)  # DEBUGGING

    for i in range(len(sorted_numbers)):
        print(sorted_numbers[i], end=", ")


if __name__ == '__main__':
    main()
