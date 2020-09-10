"""
Rhys Donaldson
CP1404 Practical 5
"""

code_dict = {"darkgoldenrod": "#b8860b", "darkturquoise": "#00ced1", "greenyellow": "#adff2f", "hotpink": "#ff69b4", "dimgray": "#696969", "firebrick": "#b22222", "lawngreen": "#7cfc00"}
colour_guess = input("Enter a colour or enter a space to exit\n >>>").lower()
while colour_guess != "":
    if colour_guess in code_dict:
        print(code_dict[colour_guess])
    else:
        print("That is not a colour I know")
    colour_guess = input("Enter a colour or enter a space to exit\n >>>").lower()
