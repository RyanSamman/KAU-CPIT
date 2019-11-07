a, b, c = eval(input("Enter a, b, c: "))

delta = b ** 2 - 4*a*c

if delta < 0:
    print("The equation has no real roots")
elif delta == 0:
    r1 = -b/(2*a)
    print("The root is", r1)
elif delta > 0:
    r1 = (-b + delta**0.5)/(2*a)
    r2 = (-b - delta**0.5)/(2*a)
    print("The roots are", r1, "and", r2)
