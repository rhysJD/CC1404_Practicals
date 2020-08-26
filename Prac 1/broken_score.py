"""
This checks the score of a person and gives a result based on the score
Rhys Donaldson
"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent") # if these are reordered it doesnt really work
elif score >= 50:
    print("Passable")
else:
    print("Bad")