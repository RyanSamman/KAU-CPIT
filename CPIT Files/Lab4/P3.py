# input
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))

# Processing
gratuityRate /= 100
interest = subtotal * gratuityRate
total = subtotal + interest

# Output
print(interest, total)
