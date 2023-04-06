class Guitar:
    """Class defined for guitars."""
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year


guitars = []
with open("guitars.csv", "r") as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

for guitar in guitars:
    guitars.sort()
    print(guitar)
