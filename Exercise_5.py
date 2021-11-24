'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
    1)Randomly generate two lists to test this
    2)Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''




def find_commons(list_a, list_b):
    a = list_a
    b = list_b
    a_set = set(a) #sets list a as variable1
    commons = a_set.intersection(b) #finds the commons between list a and list b
    list_of_commons = list(commons) #takes the list_of_commons and turns it into a list
    print(list_of_commons)

find_commons( , )
