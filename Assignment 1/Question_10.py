'''
Number guessing game 1-50 with maximum 7 attempts.
'''

import random

secret = random.randint(1, 50)
tries = 7

for i in range(tries):
    guess = int(input(f"Attempt {i+1}: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You guessed correctly!")
        break
else:
    print("Better luck next time!")
