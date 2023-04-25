def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":  # convert c to f
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        elif choice == "F":  # Convert f to c
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        else:
            print("Invalid option")
            print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
