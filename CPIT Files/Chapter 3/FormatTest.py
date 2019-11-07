x = 16.405674
# deletes anything outside 2 dp
print("x is", format(x, ".2f"))

# Keeps the string ending 10 characters from the left side of the page (right justified)
print(format(57.467657, "10.2f"))
print(format(12345678.923, "10.2f"))  # str width is over 10, so moves 1 spot, but d.p is kept at 2
print(format(57.4, "10.2f"))
print(format(57, "10.2f"))

# 10 characters from
print(format(0.0033923, "10.2%"))  # *100 and adds % to end
print(format(0.0033923, "<10.2%"))  # ^ + left justified (stuck to left side)

# ~~~~~~~~~~~~~~~~~~~~~~~~ what does d do?
print(format(59832, "10d"))
print(format(59832, "<10d"))

# anything on the left side doesnt delete, right does
print(format("Welcome to Python", "<2s"))
'''
10.2f
5d
10.2%
50s
<10.2f
>10.2f
'''
