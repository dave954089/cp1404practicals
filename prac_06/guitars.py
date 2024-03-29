"""
Playing the guitars
"""

from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    print(f"{Guitar} added.")
    name = input("Name: ")
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("------------------Snip---------------------")

print("These are my guitars:")
for g in  guitars:
    print(f"Guitar {g}: {name} ({year}), worth ${cost}")