"""

"""
def checker(score):
    if score < 0:
        return("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent") # if these are reordered it doesnt really work
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")

def main():
    score = float(input("Enter score: "))
    print(checker(score))

main()