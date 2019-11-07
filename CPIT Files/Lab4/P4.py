from decimal import *

balance, annualInterestRate = Decimal(1000), Decimal(3.5)
# eval(input("Enter balance and interest rate (e.g, 3 for # 3%): "))

interest = balance * annualInterestRate/1200
interest = round(interest, 2)

print("interest is: ",interest)
