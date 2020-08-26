"""
CP1404 - Practical
Rhys Donaldson
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input('Please enter an integer: '))
        finished = True
    except ValueError:  # TODO - add something after except
        print("That is not an integer. Please enter a valid integer.")
print("Valid result is:", result)