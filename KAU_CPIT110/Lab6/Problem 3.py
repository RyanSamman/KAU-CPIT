weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

pricePerWeight1 = weight1 / price1
pricePerWeight2 = weight2 / price2

if pricePerWeight1 > pricePerWeight2:
    print("Package 2 has the better price")
elif pricePerWeight2 > pricePerWeight1:
    print("Package 1 has the better price")
elif pricePerWeight2 == pricePerWeight1:
    print("Same price per unit weight")