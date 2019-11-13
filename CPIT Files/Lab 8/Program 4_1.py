# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


def pattern1(x):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            outstring += str(j) + " "
        outstring += "\n"
    return outstring


print(pattern1(6))
