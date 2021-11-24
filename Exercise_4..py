unum = int(input('Number: '))
llist = range(1, unum)
a = []
for i in llist:
    if unum % i == 0:
        a.append(i)
print(a)
