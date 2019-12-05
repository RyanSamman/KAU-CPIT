
def m(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i/(i+1)


def main():
    print(format("i", "<10s"), format("m(i)", "6s"))

    for i in range(1, 20 + 1):
        print(print(format(i, "<5d"), format("m(i)", "6s")))


if __name__ == '__main__':
    main()
