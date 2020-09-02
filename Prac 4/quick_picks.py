"""
CP1404 Practical 4
Rhys Donaldson
"""
import random
pickNo = int(input("How many quick picks? "))
counter = 0
numbNo = 0
while counter != pickNo:
    quikpiks = []
    for i in range(6):
        numbGen = random.randint(1, 45)
        while numbGen in quikpiks:
            numbGen = random.randint(1, 45)
        quikpiks.append(numbGen)
        quikpiks[i] = numbGen
    quikpiks.sort()
    print(quikpiks)
    counter += 1
