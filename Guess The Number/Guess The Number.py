import random

hidden = random.randrange(1, 100)

guess = int(input("Please enter your guess Between 1-100: "))

while True:
    if guess == hidden:
        print("Hit!")
        break
    elif guess < hidden:
        print("Your guess is too low")
        guess  = int(input("Please enter your guess: "))
    else:
        print("Your guess is too high")
        guess = int(input("Please enter your guess: "))
