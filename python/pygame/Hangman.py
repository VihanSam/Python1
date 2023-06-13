import time
import random

name = input("Enter your name!")
print("Hello",name)
time.sleep(1)
print("Start Guesseing!")
words = ['evening','university','education','programming','smile','answer']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed += 1
    if failed == 0:
        print("\nYOU WON!:D")
        break
    guess = input("\nGuess a character!") [0]
    guesses += guess
    if guess not in word:
        turns -= 1
        print("WRONG")
        print("You have",turns,"more guesses")
        if turns == 4:
              time.sleep(1)
              print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
        elif turns == 3:
              time.sleep(1)
              print('   _____ \n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
        elif turns == 2:
              time.sleep(1)
              print('   _____ \n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
        elif turns == 1:
              time.sleep(1)
              print('   _____ \n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      o\n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
        elif turns == 0:
              time.sleep(1)
              print('   _____ \n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      o \n'
                    '  |     /|\ \n'
                    '  |     / \ \n'
                    '__|__ \n')
        if turns == 0:
            print("YOU LOST The right answer is",word)