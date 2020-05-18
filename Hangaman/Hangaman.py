import random
from hangmanproccess import ProccessOfHangman

game = True
while game:
    count = 0
    progress = ''
    play = ''
    Word = random.choice(open('randomword.txt').read().split("\n"))
    Word = Word.upper()
    for i in Word:
        progress += '_'

    print('\nWelcome to Hangman!!!')
    print("\n" + progress)
    while True:
        guess = input("Enter the letter: ").upper()
        if guess in Word:
            print(guess + " is correct Word")
            for i in range(0, len(Word)):
                if guess == Word[i]:
                    progress = progress[:i] + guess + progress[i + 1:]
        elif guess not in Word:
            print(guess + " is not in the word!!")
            count += 1

        print(ProccessOfHangman(count))

        print(progress)

        if count == 7:
            print("You loss the game. Sorry!!")
            print("The Word is :" + Word)
            play = input("Do you Want to play again!(y/n)").upper()
            break
        elif progress == Word:
            print("You Won the Game")
            play = input("Do you Want to play again!(y/n)").upper()
            break

    if play != 'Y':
        game = False

