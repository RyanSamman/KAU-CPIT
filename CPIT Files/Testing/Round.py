from decimal import *

balance, annualInterestRate = Decimal(1000), Decimal(3.5)
# eval(input("Enter balance and interest rate (e.g, 3 for # 3%): "))


interest = interest2 = balance * annualInterestRate/1200
print(interest)
interest = round(interest, 2)

print("interest is: ",interest)

# Instead of using floating point #s which are inaccurate
interest2 *= 100
interest2 = int(interest2)/100
print("interest 2 is: ", interest2)
