loanAmount = 10000  # eval(input("Enter a loan amount, for example 120000.95: "))
numberOfYears = 1  # eval(input("Enter number of years as an integer, for example 5: "))

print("\n" + format("Interest Rate", "<20s") + format("Monthly Payment", "23s") + format("Total Payment", "20s"))

for i in range(24 + 1):
    annualInterestRate = (5 + (1/8) * i)/100

    monthlyInterestRate = annualInterestRate / 12

    monthlyPayment = ((loanAmount * monthlyInterestRate)
                      /(1 - (1 / (1 + monthlyInterestRate))**(numberOfYears * 12)))

    totalPayment = monthlyPayment * numberOfYears * 12

    print(format(annualInterestRate*100, "5.3f") + " % " + format(monthlyPayment, ">20.2f") + format(totalPayment, ">25.2f"))

    # print("%s               %s                 %s"
    # % ((format(annualInterestRate, "4.3f") + " %"), format(monthlyPayment, "6.2f"), format(totalPayment, ">8.2f")))
