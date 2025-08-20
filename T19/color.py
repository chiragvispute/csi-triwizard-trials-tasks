# Task: Display spells in the terminal with different colors using colorama

from colorama import init, Fore
init(autoreset=True)

spells = {
    "Lumos": "Good",
    "Avada Kedavra": "Dark",
    "Expelliarmus": "Good",
    "Crucio": "Dark",
    "Alohomora": "Neutral"
}

# TODO: Loop through each spell
# - Print Good spells in GREEN
# - Print Dark spells in RED
# - Print Neutral spells in YELLOW
# Hint: Use spells[spell] to get the type

