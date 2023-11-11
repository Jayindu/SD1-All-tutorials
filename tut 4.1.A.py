hidden=6
guess_num=int(input("enter number between 1-20 = "))
while guess_num != hidden:
    print("guess number is not correct")
    guess_num=int(input("enter number between 1-20 = "))
print("guessed number is corrcet")