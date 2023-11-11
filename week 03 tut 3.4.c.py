cost_meal=0

satisfaction=0

cost_meal=float(input("Enter cost of the meal = "))
satisfaction=int(input("(Totally satisfied =2\nSatisfied = 2 \nDissatisfied = 3)\nEnter satisfaction level using above rating = "))
if satisfaction==1:
    tip=cost_meal*20/100
elif satisfaction==2:
    tip=cost_meal*15/100
elif satisfaction==3:
    tip=cost_meal*10/100
else:
    print("Enter Valid Rating")
print("Sarisfaction level is = ",satisfaction)
print("Tip is = ",tip)