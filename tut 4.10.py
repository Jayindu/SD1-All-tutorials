import random
hidden=random.randint(1,20)
num_of_guess=0
guess=int(input("enter number between 1-20 = "))
while num_of_guess<5:
    guess=int(input("enter number between 1-20 = "))
    num_of_guess+=1
    if guess==hidden:
        print("You correct")
        break
    elif guess<=hidden:
        print("Your guess number is lower")
    else:
        print("Your guess number is higher")
    
    
    
