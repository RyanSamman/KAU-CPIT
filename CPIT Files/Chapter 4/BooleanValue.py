x = 10 > 20 # False
y = 10 < 20 # True

print('x =', x)
print('y =', y)

x = int(False)  # 0
y = int(True)  # 1
print(x, y)

x = bool(0)  # if the number is 0, it will be false
y = bool(1)  # any number not 0 will be true
print(x, y)

x = bool(-25)
y = bool(2000)
print(x, y)
