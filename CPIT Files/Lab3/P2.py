# Prompts user to input the number of minutes they want to convert
minutes = eval(input("Enter the number of minutes: "))

# 1 hour is 60 minutes
# 1 day is 24 hours
# 1 year is 365 days

# Processing input
calculatedDays = int(minutes / (60*24))
calculatedYears = int(calculatedDays / 365)
calculatedDays %= 365

# Outputs Years and Days
print(minutes,"minutes is approximately",calculatedYears,"years and",calculatedDays,"days")

