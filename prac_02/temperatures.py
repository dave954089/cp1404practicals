def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":  # convert c to f
            convert_celcius()
        elif choice == "F":  # Convert f to c
            convert_fahrenheit()
        else:
            print("Invalid option")
            print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def convert_celcius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
