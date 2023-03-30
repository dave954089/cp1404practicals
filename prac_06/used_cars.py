"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My car")
    limo = Car(100, "Limo")  # new car limo added
    my_car.drive(30)
    limo.add_fuel(20)  # fuel added to car
    limo.drive(115)  # distance car driven for.
    print(f"Car has fuel: {my_car.fuel}")
    print(f"limo has fuel: {limo.fuel}")

    print(my_car)
    print(limo)


main()