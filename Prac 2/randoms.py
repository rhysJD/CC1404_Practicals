'''
CP1404 - Practical 2
Rhys Donaldson
'''

import random

print(random.randint(5,20))
# It spit out 13, but it could have been any integer from 5 to 20 inclusive
print(random.randrange(3, 10, 2))
#It gave me a 9, and it could have beenand integer between 3 and 9 inclusive. 4 is a possibility here.
print(random.uniform(2.5, 5.5))
#gave me 4.531538316437027. It could have been any number, not just integers, between 2.5 and 5.5

print(random.randint(1, 100))
