"""
CP1404 - Practical 2
Rhys Donaldson
"""

totalNumb = 0

names = open('name.txt', 'w')
print(input("What is your name? "), file= names)
names.close()

names = open('name.txt', 'r')
print('Your name is', names.readline())
names.close()

numbersTXT = open('numbers.txt', 'r')
numb1 = int(numbersTXT.readline())
numb2 = int(numbersTXT.readline())
print(numb1 + numb2)
numbersTXT.close()

numbersTXT = open('numbers.txt', 'r')
numbersList = list(numbersTXT.readlines())
for i in range(0, len(numbersList)):
    totalNumb = totalNumb + int(numbersList[i])
print(totalNumbr)
numbersTXT.close()