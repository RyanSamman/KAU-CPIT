integer = -1
total_integer = positives = negatives = loops = 0
Continue = True

while Continue:
    integer = eval(input("Enter an integer, the input ends if it is 0: "))

    if integer == 0:
        Continue = False
        break
    if integer > 0:
        positives += 1
    if integer < 0:
        negatives += 1
    loops += 1
    total_integer += integer

if total_integer == 0:
    print("You didn't enter any number")
else:
    print("The number of positives is", positives)
    print("The number of negatives is", negatives)
    print("The total is", total_integer)
    print("The average is", total_integer/loops)