# input
investmentAmount = eval(input("Enter investment amount: "))
monthlyInterestRate = eval(input("Enter annual interest rate: "))/(100*12)
numberOfMonths = eval(input("Enter number of years: ")) * 12

# processing
futureInvestmentValue = investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)

# output
print("Accumulated value is", futureInvestmentValue)
