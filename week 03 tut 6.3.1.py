num=0
num1=0
sym="+","-","*","/"
ans=0

num=float(input("enter number = "))
sym=str(input("enter operator(+,-,*,/) = "))

if sym=="+":
    num1=float(input("enter number = "))
    ans=num+num1
    print("answer is = ",ans)
elif sym=="-":
    num1=float(input("enter number = "))
    ans=num-num1
    print("answer is = ",ans)
elif sym=="*":
    num1=float(input("enter number = "))
    ans=num*num1
    print("answer is = ",ans)
else:
    sym=="/"
    num1=float(input("enter number = "))
    if num1==0:
        print("Zerodivision Error")
    else:
        ans=num/num1
        print("answer is = ",ans)

#answers

#enter number = 5
#enter operator(+,-,*,/) = /
#enter number = 0
#Zerodivision Error