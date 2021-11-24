'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. 
Extras:
    1)If the number is a multiple of 4, print out a different message.
    2)Ask the user for two numbers: one number to check (call it num) 
    and one number to divide by (check). If check divides evenly into num, 
    tell that to the user. If not, print a different appropriate message.
'''
##pt 1
unum = int(input("Number: "))
if unum % 2 == 0:
    print(f'{unum} is even')
    if unum % 4 == 0:
        print(f"{unum} is a mulitple of 4")
else:
    print(f"{unum} is odd")

##pt 2 (extra #2)
num = int(input('First Number: '))
check = int(input('Second Number: '))
if num % check == 0:
    print(f'Your first number {num} is divisable into your second number {check}')
else:
    print(f'Your first number {num} is not divisable into your second number {check}')
