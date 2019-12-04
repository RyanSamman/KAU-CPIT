

def displaySortedNumbers2(args, sort):
    count = 0

    if sort == max:
        while count < len(args) + 50:
            for i in range(len(args) - 1):
                if eval(args[i + 1]) > eval(args[i]):
                    # print(args[i], args[i+1])
                    args[i], args[i+1] = args[i + 1], args[i]
    elif sort == min:
        while count < len(args) + 50:
            for i in range(len(args) - 1):
                if eval(args[i + 1]) > eval(args[i]):
                    # print(args[i], args[i + 1])
                    args[i], args[i + 1] = args[i + 1], args[i]
    else:
        print("Input valid sort method")
        count += 1
    return args


def main():
    sort = min
    in_string = input("Enter numbers to be sorted: ")
    in_string = in_string.split(", ")

    sorted_numbers = displaySortedNumbers2(in_string, sort)
    print(sorted_numbers)

    for i in range(len(sorted_numbers)):
        print(sorted_numbers[i], end=", ")


if __name__ == '__main__':
    main()
