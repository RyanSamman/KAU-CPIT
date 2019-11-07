

def is_prime(integer):
    if integer < 2:
        return False
    if integer == 2:
        return True
    else:
        for divider in range(2, integer):
            dividable = integer % divider == 0
            if dividable:
                return False
        return True


i = numberOfPrime = 0

while numberOfPrime < 50:  # for i in range(0, 230):
    if is_prime(i):
        print(format(i, "6d"), end="")
        numberOfPrime += 1
        if (numberOfPrime % 10) == 0:
            print()
    i += 1
