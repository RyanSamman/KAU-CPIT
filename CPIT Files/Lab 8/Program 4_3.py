#           1
#         2 1
#       3 2 1
#     4 3 2 1
#   5 4 3 2 1
# 6 5 4 3 2 1


def pattern3(x):
    outstring = ""
    for i in range(1, x + 1):
        for j in range(1, x + 1 - i):
            outstring += "  "
        for k in range(i, 0, -1):
            outstring += str(k) + " "
        outstring += "\n"
    return outstring


print(pattern3(6))
