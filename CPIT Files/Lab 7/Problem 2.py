value_kilogram = 1
value_pound = 20

print(format("kilograms", "16s") + format("pounds", "13s") + "|" +
      format("pounds", ">12s") + format("kilograms", ">15s"))
print("-"*58)

while value_kilogram < 200:
    print(format(value_kilogram, "<16d") + format(value_kilogram * 2.2, ">6.1f") + "       |      " +
          format(value_pound, "<6d") + format(value_pound*0.45, ">15.2f"))
    value_kilogram += 2
    value_pound += 5

