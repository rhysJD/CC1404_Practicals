"""
CP1404/CP5632 - Practical, this one converts temperatures
Rhys Donaldson
"""


def celcius_to_fahrenheit(temperature):
    fahrenheit = temperature * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celcius(temperature):
    celsius = 5.0 / 9 * (temperature - 32)
    return celsius

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = float(input("Celsius: "))
            temperature_conv = celcius_to_fahrenheit(temperature)
            print("Result: {:.2f} F".format(temperature_conv))
        elif choice == "F":
            temperature = float(input("Fahrenheit: "))
            temperature_conv = fahrenheit_to_celcius(temperature)
            print("Result: {:.2f} C".format(temperature_conv))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()