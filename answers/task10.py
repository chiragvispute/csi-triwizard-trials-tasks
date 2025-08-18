from colorama import init, Fore

init(autoreset=True)

spells = {
    "Lumos": "Good",
    "Avada Kedavra": "Dark",
    "Expelliarmus": "Good",
    "Crucio": "Dark",
    "Alohomora": "Neutral"
}

for spell in spells:
    if spells[spell] == "Good":
        print(Fore.GREEN + spell + " -> Good")
    elif spells[spell] == "Dark":
        print(Fore.RED + spell + " -> Dark")
    else:
        print(Fore.YELLOW + spell + " -> Neutral")
