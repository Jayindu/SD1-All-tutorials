hidden=6
import random
guess_num=int(input("guess a number = "))
while guess_num != hidden:
    if guess_num<hidden:
        print("guess number is too low")
    else:
        print("guess number is too high")
    guess_num=int(input("guess a number = "))
print("guessed number is corrcet")