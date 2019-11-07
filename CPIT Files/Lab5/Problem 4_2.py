inputInteger = 1234 #eval(input("Enter an integer: "))
integer1 = str(inputInteger // 1000)
inputInteger %= 1000
integer2 = str(inputInteger // 100)
inputInteger %= 100
integer3 = str(int(inputInteger / 10))
inputInteger %= 10
integer4 = str(inputInteger)

print("The reversed number is " + integer4 + integer3 + integer2 + integer1)
