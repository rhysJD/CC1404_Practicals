"""
CP1404 Practical 10
Rhys Donaldson 13581558
5/11/2020
"""

import wikipedia
choice = input("What would you like to search for?\n>>>")
while choice is not "":
    try:
        choice = wikipedia.page(choice)
        print(choice.title + "\n" + choice.summary + "\n" + choice.url)
        choice = input("What would you like to search for?\n>>>")
    except wikipedia.exceptions.DisambiguationError:
        choice = input("That page is a disambiguation. Please pick a different choice \n>>>")
print("Goodbye!")
