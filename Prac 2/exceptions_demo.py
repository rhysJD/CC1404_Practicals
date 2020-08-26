"""
CP1404 - Practical 2
Rhys Donaldson
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator cannot be zero. PLease enter a new number: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Q1: ValueError occurs when the input is not an integer. Putting in symbols, letter, or decimals will get this number
#Q2: This occurs when the denominator is zero and the program attempts to divide by it. Fixed by checking that it doesnt contain a zero, and asking for a new input if it does.