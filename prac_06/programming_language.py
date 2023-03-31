class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=0):
        """Assigning constructors"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Str for calling """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Dynamic function"""
        return self.typing == "Dynamic"
