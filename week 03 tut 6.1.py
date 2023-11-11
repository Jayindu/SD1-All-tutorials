try:
    n = input('Give me a number over 100: ')
    n = int(n)
    if n <= 100:
        print(n, 'is not over 100')
    else:
        print(n, "is over 100")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


#answers

#Give me a number over 100: 200
#200 is over 100

#Give me a number over 100: 50
#50 is not over 100

#Give me a number over 100: 656.65
#Invalid input. Please enter a valid integer.