
# Input
weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

# Processing
weight *= 0.45359237
height *= 0.0254

BMI = weight / (height ** 2)

print("BMI is", BMI)