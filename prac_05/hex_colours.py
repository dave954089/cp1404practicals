"""
CP1404/CP5632 Practical
hex colors
"""

COLORS_IN_HEX = {"AbsoluteZero": "0048ba", "AcidGreen": "b0bf1a", "AliceBlue": "f0f8ff", "AlizarinCrimson": "e32636",
                 "Amaranth": "e52b50", "Amber": "ffbf00", "Amethyst": "9966cc", "AntiqueWhite": "faebd7",
                 "Apricot": "fbceb1", "Aqua": "00ffff"}

print("----------Hex Colors----------")
color_name = input("Enter enter color name: ")
while color_name !=  "":
    print(color_name, "is", COLORS_IN_HEX.get(color_name))
    color_name = input("Enter enter color name: ")
else:
    print("BYE")
