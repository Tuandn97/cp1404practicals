"""
CP1404/CP5632 Practical
Finding color code
Word Occurrences
Estimate: 8 minutes
Actual:   10 minutes
"""

COLOR_TO_CODE = {"Absolute Zero": '#0048ba', "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Army Green": "	#4b5320"}
color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        color_code = COLOR_TO_CODE[color_name]
        print(f"{color_name}:{color_code}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()

