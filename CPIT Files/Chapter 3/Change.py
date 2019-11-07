from decimal import *
totalPennies = eval(format(input("Insert $ in the form (10.03): ")),".2f")

dollars = totalPennies // 100
remainingPennies = totalPennies % 100

quarters = remainingPennies // 25
remainingPennies %= 25

dimes = remainingPennies // 10
remainingPennies %= 10

nickels = remainingPennies // 5
remainingPennies %= 5


print(totalPennies / 100, "is:\n\t",
      int(dollars), "dollars,\n\t",
      int(quarters), "quarters,\n\t",
      int(dimes), "dimes,\n\t",
      int(nickels), "nickels, and\n\t",
      int(remainingPennies), "pennies")