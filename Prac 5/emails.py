"""
CP1404 Practical 5
Rhys Donaldson
"""

emails = {}
in_email = str(input("Email: "))
in_names = in_email.split("@")
in_names = in_names[0].split(".")
name = " ".join(in_names).title()
name_yn = input("Is your name {}? (Y/n)".format(name))
while name_yn != 'Y':
    name = str(input("Name: "))
    name_yn = "Y"
emails[name] = in_email
print(emails)
