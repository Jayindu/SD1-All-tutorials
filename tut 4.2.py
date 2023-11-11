total=0
count=0
score=0
while score!=-9:
    score = int(input("Enter score, (Enter -9 to end): "))
    total+=score
    count+=1
if count>0:
    average=float(total)/count
    print("Average is ",average)
else:
    print("No scores enterd")


#answer

#Enter score, (Enter -9 to end): -9
#Average is  -9.0