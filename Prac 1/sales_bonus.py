"""
Calculates the bonus an employee gets based on the total sale amount
Rhys Donaldson

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input('Enter sale value: $'))
while sales > 0:
    if sales <= 1000:
        bonus = sales * 0.1
    elif sales > 1000:
        bonus = sales * 0.15 # I had this multiplier and the message for each amount but though it was unnecessary
    print("The total bonus is: ${:.2f}".format(bonus))
    sales = float(input('Enter sale value: $'))
print('Invalid number')
