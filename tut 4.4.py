num=0
total=0
for num in range(5):
    try:
        num=int(input("Enter number = "))
        total+=num
    except ValueError:
        print("Invalid Input Enter valid number")
print("Total is ",total)