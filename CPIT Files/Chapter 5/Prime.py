prime = [1,2]
length = 0
i = 0
z = 0
while length <= 5:
    i += 1
    for x in range(1, i+1):
        if i % x == 0:
            z += 1
            continue
        if z == 2:
            print(i)
            prime += [i]
            length = len(prime)
            z = 0
        else:
            z = 0

print(prime)