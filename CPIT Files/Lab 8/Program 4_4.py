# 1 2 3 4 5 6
#   1 2 3 4 5
#     1 2 3 4
#       1 2 3
#         1 2
#           1


def pattern4(x):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, i):
            outstring += "  "
        for k in range(1, x + 2 - i):
            outstring += str(k) + " "
        outstring += "\n"
    return outstring


print(pattern4(6))
