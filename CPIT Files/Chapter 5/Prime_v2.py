x = 6
length = divided = 0
prime = []

while length <= 50:
    for i in range(2, x):
        if x % i == 0:
            divided += 1
    if divided == 0:
        prime += [x]
        print(x)
    length = len(prime)

print(prime)