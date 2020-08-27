"""
CP1404 Practical 4
Rhys Donaldson 13581558
"""
numbers = []

for i in range (0, 5):
    numb = float(input('Number:'))
    numbers.append(numb)
print("The first number is {:.2}".format(numbers[0]))
print("The last number is {:.2}".format(numbers[len(numbers) - 1]))
print("The samllest number is {:.2}".format(min(numbers)))
print("The largest number is {:.2}".format(max(numbers)))
print("The average of the numbers is {:.2}".format(sum(numbers) / 5))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
users_name = str(input('Please enter username:'))
while users_name not in usernames:
    print("Access Denied")
    users_name = input('Please enter username: ')
print("Access Granted")
