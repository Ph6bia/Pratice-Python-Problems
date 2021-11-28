'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they 
guessed too low, too high, or exactly right.
'''

import random
game_over = False
print('Welcome to the Number Guessing Game!')
while not game_over:
    guesses = 0
    num = random.randint(1, 9)
    while True:
        uguess = int(input('Guess: '))
        if uguess > num:
            guesses += 1
            print('Too high! Try again.')
            continue
        elif uguess < num:
            guesses += 1
            print('Too low! Try again.')
            continue
        elif uguess == num:
            guesses += 1
            print(f'Correct! You got it in {guesses} tries!')
            guesses = 0
            num = random.randint(1, 9)
            uexit = input('Type exit to exit, type anything else to continue. ')
            if uexit.lower() == 'exit':
                game_over = True
            else:
                continue
        else:
            print('Error')
            break
