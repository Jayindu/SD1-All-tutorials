mark=0
mark=float(input("Enter marks = "))
if 0<=mark<=100:
    if mark >= 70:
        print("Exceptional result!")
    elif mark >= 40:
        print("Satisfactory result!")
    else:
        print("You have failed.")
else:
    print("Invalid Mark")

#answers

# -1,101 = Invalid Mark
# 1,0,39 = You have failed.
# 40,41,69 = Satisfactory result!
# 70,71,99,100 = Exceptional result!
