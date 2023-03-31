"""
CP1404
prac_06
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Assigning constructors"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Str for calling """
        return f"{self.name}  ({self.year}) : {self.cost}"

    def get_age(self):
        """To find the age"""
        age = (CURRENT_YEAR - self.year)
        return age

    def is_vintage(self):
        """to find if vintage"""
        return self.get_age() >= VINTAGE_AGE




