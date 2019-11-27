

def displaySortedNumbers2(args):
    count = 0
    while count < len(args) + 50:
        for i in range(len(args) - 1):
            if eval(args[i + 1]) > eval(args[i]):
                print(args[i], args[i+1])
                args[i], args[i+1] = args[i + 1], args[i]
        count += 1
    return args


def main():
    in_string = "3, 2.4, 5, 50, 6, 4" #input("Enter numbers to be sorted: ")
    in_string = in_string.split(", ")

    sorted_numbers = displaySortedNumbers2(in_string)
    #print(sorted_numbers)
    for i in range(len(sorted_numbers)):
        print(sorted_numbers[i], end=", ")


if __name__ == '__main__':
    main()
