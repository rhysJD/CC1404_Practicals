'''
Loops, just a bunch of loops that all happen
Rhys Donaldson
'''


for i in range(1, 21, 2):
    print(i, end=' ')
print() # range(start, stop. step)

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print() #start at 20, step by -1, stop at 0

stars = int(input("How many stars? "))
for i in range(0, stars, 1):
    print('*', end='')
print()

baseStar = 1
while baseStar <= stars:
    for i in range(0, baseStar, 1):
        print('*', end='')
    print()
    baseStar = baseStar + 1
#the while loop continually prints larger lines of stars until it hits the number entered, then stops