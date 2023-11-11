dis1=0
dis2=0
num_rolls=100
doubled_rolls=0
import random
for num_rolls in range(0,num_rolls):
    dis1=random.randint(1,7)
    dis2=random.randint(1,7)

    if dis1==dis2:
        doubled_rolls+=1

print("Number of rolls = ", num_rolls)
print("Number of doubles = ", doubled_rolls)
