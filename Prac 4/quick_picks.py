"""
CP1404 Practical 4
Rhys Donaldson
"""
import random
pickNo = int(input("How many quick picks? "))
counter = 0
numbNo = 0
while counter != pickNo:
    quik_piks = []
    for i in range(6):
        numbGen = random.randint(1, 45)
        while numbGen in quik_piks:
            numbGen = random.randint(1, 45)
        quik_piks.append(numbGen)
        quik_piks[i] = numbGen
    quik_piks.sort()
    print(quik_piks)
    counter += 1
