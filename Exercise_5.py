def find_commons(list_a, list_b):
    a = list_a
    b = list_b
    a_set = set(a) #sets list a as variable1
    commons = a_set.intersection(b) #finds the commons between list a and list b
    list_of_commons = list(commons) #takes the list_of_commons and turns it into a list
    print(list_of_commons)

find_commons( )
