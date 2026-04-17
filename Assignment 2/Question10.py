'''
Dice guessing game with smiling face for correct and neutral face for off by 1.
'''

import random

dice = random.randint(1, 6)
guess = int(input("Guess the dice value (1-6): "))

print("Dice rolled:", dice)

if guess == dice:
    print("😊")  # correct guess
elif abs(guess - dice) == 1:
    print("😐")  # off by 1
else:
    print("😢")  # sad face 
