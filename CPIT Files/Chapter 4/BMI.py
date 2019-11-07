weight = eval(input("Enter weight in pounds: ")) #* 0.45359237
height = eval(input("Enter height in inches: ")) #* 0.0254

bmi = weight / (height ** 2)
print("BMI is", format(bmi,".2f"))

if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
