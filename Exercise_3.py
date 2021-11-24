##pt 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        print(i)
        b.append(i)
print(b)

##pt 2 (extra #3)
unum = int(input('Number: '))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < unum:
        b.append(i)
print(b)
