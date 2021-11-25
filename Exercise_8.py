'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of 
congratulations to the winner, and ask if the 
players want to start a new game).
'''

while True:
    p1_answer = str(input('Player 1: Rock, Paper, or Scissors? '))
    
    if p1_answer.lower() == 'rock':
        pass
    elif p1_answer.lower() == 'paper':
        pass
    elif p1_answer.lower() == 'scissors':
        pass
    else:
        print('Not vald answer, please try again.')
        continue

    p2_answer = input('Player 2: Rock, Paper, and Scissors? ')
    
    if p2_answer.lower() == 'rock':
        pass
    elif p2_answer.lower() == 'paper':
        pass
    elif p2_answer.lower() == 'scissors':
        pass
    else:
        print('Not vald answer, please try again.')
        continue

    if p1_answer.lower() == p2_answer.lower():
        again = input('Tie!, try again(y/n)? ').lower()
        if again == 'n':
            break
        else:
            continue
    elif p1_answer.lower() == 'rock' and p2_answer.lower() == 'paper':
        again = input('Player 2 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    elif p1_answer.lower() == 'rock' and p2_answer.lower() == 'scissors':
        again = input('Player 1 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    elif p1_answer.lower() == 'scissors' and p2_answer.lower() == 'paper':
        again = input('Player 1 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    elif p1_answer.lower() == 'scissors' and p2_answer.lower() == 'rock':
        again = input('Player 2 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    elif p1_answer.lower() == 'paper' and p2_answer.lower() == 'rock':
        again = input('Player 1 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    elif p1_answer.lower() == 'paper' and p2_answer.lower() == 'scissors':
        again = input('Player 2 Wins!, try again(y/n)? ').lower()
        if again == 'n':
            break
    else:
        print('Error, Please try again.')
        continue
