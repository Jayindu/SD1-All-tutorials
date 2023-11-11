hidden=6
import random
guess_num=random.randint(1,20)
while guess_num != hidden:
    print("guess number is not correct")
    guess_num=random.randint(1,20)
print("guessed number is corrcet")