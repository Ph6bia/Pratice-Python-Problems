'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:
  1)Add on to the previous program by asking the user for another 
  number and printing out that many copies of the previous message.
  2)Print out that many copies of the previous message on separate lines.
 '''

name = input('Name: ')
age = int(input('Age: '))
yth = 100 - age #Years 'till hundred
yoh = yth + 2021 #Year of hundred, 2021 current year
print(f'{name}, you will turn 100 in the year {yoh}!')
copies = int(input(f'How many copies would you like {name}? '))
print(f'{name}, you will turn 100 in the year {yoh}! \n' * copies)
