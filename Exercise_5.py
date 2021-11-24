a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a_set = set(a) #sets list a as variable1
commons = a_set.intersection(b) #finds the commons between list a and list b
list_of_commons = list(commons) #takes the list_of_commons and
print(list_of_commons)
