'''
Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that 
divides evenly into another number. For example, 
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

unum = int(input('Number: '))
llist = range(1, unum)
a = []
for i in llist:
    if unum % i == 0:
        a.append(i)
print(a)