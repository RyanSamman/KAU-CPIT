tuition = eval(input("Insert Current tuition: "))
inflation = eval(input("Insert Current inflation: "))/100
futureTuition = tuition
years = 0
while futureTuition <= (tuition * 2):
    futureTuition *= (1 + inflation)
    years += 1

print("it will take",years,"years for tuition to double to", format(futureTuition,".2f"))