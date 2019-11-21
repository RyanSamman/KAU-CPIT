name = "Smith"#input("Enter employee's name: ")
hours = 10#eval(input("Enter number of hours worked in a week: "))
payRate = 9.75#eval(input("Enter hourly pay rate: "))
taxFederal = 0.20#eval(input("Enter federal tax withholding rate: "))
taxState = 0.09#eval(input("Enter state tax withholding rate: "))

payGross = hours * payRate
payNet = payGross * (1 - (taxFederal + taxState))

out = "Employee Name: " + name + "\n"
out += "Hours worked: " + format(hours, ".1f") + "\n"
out += "Pay Rate: " + format(payRate, ".2f") + "\n"
out += "Gross Pay: " + format(payGross, ".1f") + "\n"
out += "Deductions: " + "\n"
out += "  Federal Withholding (" + format(taxFederal, ".1%") + "): $" + format(payGross * taxFederal, ".2f") + "\n"
out += "  State Withholding (" + format(taxState, ".1%") + "): $" + format(payGross * taxState, ".2f") + "\n"
out += "  Total Deduction: $" + format(payGross * (taxState + taxFederal), ".2f") + "\n"
out += "Net Pay: $" + format(payNet, ".2f")

print(out)