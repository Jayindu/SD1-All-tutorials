#a)
tempc=0
tempf=0
num=0
num=int(input("Enter number 1 to calculate  from Celsius to Fahrenheit , number 2 to calculate from Fahrenheit to Celsius = "))
if num==1:
    tempc=float(input("Enter temperature in celsius = "))
    tempf= (tempc * 1.8) + 32
    print("temperature in Fahrenheit is = ",tempf)
elif num==2:
    tempf=float(input("Enter temperature in Fahrenheit = "))
    tempc = (tempf - 32) / 1.8
    print("temperature in celsius is = ",tempc)
else:
    print("invalid option enterd" )




