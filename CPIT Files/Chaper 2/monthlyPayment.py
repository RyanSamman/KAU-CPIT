
y = ""
while y != "No":

    loanAmount = eval(input("\nLoan Amount: "))
    monthlyInterestRate = (eval(input("Yearly Interest Rate: ")) / (12*100))
    numberOfYears = eval(input("Number of Years: "))

    monthlyPayment = ((loanAmount * monthlyInterestRate) / (1 - 1 / ((1 + monthlyInterestRate)**(numberOfYears*12))))
    totalPayment = monthlyPayment * numberOfYears * 12

    print("\nMonthly Payment: ", round(monthlyPayment, 2),
          "\nTotal Payment:", round(totalPayment, 2))
    y = input("Continue?: ")
