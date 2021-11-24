'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

def is_palindrome(word):
    if word == word[::-1]:
        print(f'Your word {word} is a palindrome.')
    else:
        print(f'Your word {word} is not a palindrome.')

is_palindrome(' ')
