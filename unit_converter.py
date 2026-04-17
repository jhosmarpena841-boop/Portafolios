## unit_converter.py - Convert between different units
# Author: jhosmar
# Date: 2026-04-17

import time

def length_converter():
    while True:
        print("\n=== LENGTH CONVERTER ===")
        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        print("3. Meters to Miles")
        print("4. Miles to Meters")
        print("5. Meters to Feet")
        print("6. Feet to Meters")
        print("7. Back to main menu")
# Author: jhosmar
        option = input("Choose an option: ")

        if option == "1":
            m = float(input("Enter meters: "))
            km = m / 1000
            print(f"{m} meters = {km} kilometers")
            time.sleep(2)

        elif option == "2":
            km = float(input("Enter kilometers: "))
            m = km * 1000
            print(f"{km} kilometers = {m} meters")
            time.sleep(2)

        elif option == "3":
            m = float(input("Enter meters: "))
            miles = m / 1609.34
            print(f"{m} meters = {miles} miles")
            time.sleep(2)

        elif option == "4":
            miles = float(input("Enter miles: "))
            m = miles * 1609.34
            print(f"{miles} miles = {m} meters")
            time.sleep(2)

        elif option == "5":
            m = float(input("Enter meters: "))
            feet = m * 3.28084
            print(f"{m} meters = {feet} feet")
            time.sleep(2)

        elif option == "6":
            feet = float(input("Enter feet: "))
            m = feet / 3.28084
            print(f"{feet} feet = {m} meters")
            time.sleep(2)

        elif option == "7":
            break
# Author: jhosmar
        else:
            print("Invalid option. Try again.")
            time.sleep(2)

def weight_converter():
    while True:
        print("\n=== WEIGHT CONVERTER ===")
        print("1. Grams to Kilograms")
        print("2. Kilograms to Grams")
        print("3. Grams to Pounds")
        print("4. Pounds to Grams")
        print("5. Kilograms to Pounds")
        print("6. Pounds to Kilograms")
        print("7. Back to main menu")
# Author: jhosmar
        option = input("Choose an option: ")

        if option == "1":
            g = float(input("Enter grams: "))
            kg = g / 1000
            print(f"{g} grams = {kg} kilograms")
            time.sleep(2)

        elif option == "2":
            kg = float(input("Enter kilograms: "))
            g = kg * 1000
            print(f"{kg} kilograms = {g} grams")
            time.sleep(2)

        elif option == "3":
            g = float(input("Enter grams: "))
            lb = g / 453.592
            print(f"{g} grams = {lb} pounds")
            time.sleep(2)

        elif option == "4":
            lb = float(input("Enter pounds: "))
            g = lb * 453.592
            print(f"{lb} pounds = {g} grams")
            time.sleep(2)

        elif option == "5":
            kg = float(input("Enter kilograms: "))
            lb = kg * 2.20462
            print(f"{kg} kilograms = {lb} pounds")
            time.sleep(2)

        elif option == "6":
            lb = float(input("Enter pounds: "))
            kg = lb / 2.20462
            print(f"{lb} pounds = {kg} kilograms")
            time.sleep(2)

        elif option == "7":
            break

        else:
            print("Invalid option. Try again.")
            time.sleep(2)

def temperature_converter():
    while True:
        print("\n=== TEMPERATURE CONVERTER ===")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Back to main menu")
# Author: jhosmar
        option = input("Choose an option: ")

        if option == "1":
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C = {f}°F")
            time.sleep(2)

        elif option == "2":
            c = float(input("Enter Celsius: "))
            k = c + 273.15
            print(f"{c}°C = {k}K")
            time.sleep(2)

        elif option == "3":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F = {c}°C")
            time.sleep(2)

        elif option == "4":
            f = float(input("Enter Fahrenheit: "))
            k = (f - 32) * 5/9 + 273.15
            print(f"{f}°F = {k}K")
            time.sleep(2)

        elif option == "5":
            k = float(input("Enter Kelvin: "))
            c = k - 273.15
            print(f"{k}K = {c}°C")
            time.sleep(2)

        elif option == "6":
            k = float(input("Enter Kelvin: "))
            f = (k - 273.15) * 9/5 + 32
            print(f"{k}K = {f}°F")
            time.sleep(2)
# Author: jhosmar
        elif option == "7":
            break

        else:
            print("Invalid option. Try again.")
            time.sleep(2)

def main():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
# Author: jhosmar
        option = input("Choose a category: ")

        if option == "1":
            length_converter()
        elif option == "2":
            weight_converter()
        elif option == "3":
            temperature_converter()
        elif option == "4":
            print("See you later!")
            break
        else:
            print("Invalid option")
            time.sleep(2)

if __name__ == "__main__":
    main()
# Author: jhosmar
