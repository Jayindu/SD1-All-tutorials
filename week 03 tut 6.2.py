try:    
    age = input('Enter your age: ')
    age = int(age)
    if age >= 18:
        print("You can vote")
    else:
        print("you can't vote")
except ValueError:
    print("Invalid input. Please enter a valid integer.")        

#answers

#Enter your age: 15
#you can't vote

#Enter your age: 20
#You can vote

#Enter your age: 12.5
#Invalid input. Please enter a valid integer.