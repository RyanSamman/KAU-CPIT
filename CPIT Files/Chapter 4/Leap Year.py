year = eval(input("Insert Year: "))

isLeapYear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print("is", year, "a leap year?", isLeapYear)