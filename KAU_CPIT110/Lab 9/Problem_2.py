def m(i):
    sum = 0
    for i in range(1, i + 1):
        sum += i/(i+1)
    return sum


def main():
    rows = 20
    print(format("i", "<10s"), format("m(i)", "<10s"))

    for n in range(1, rows +1):
        print(format(n, "<10d"), format(m(n), "6.4f"))


if __name__ == '__main__':
    main()
