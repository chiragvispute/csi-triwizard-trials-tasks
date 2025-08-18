from playsound import playsound

spells = {
    "Lumos": "lumos.mp3",
    "Expelliarmus": "expelliarmus.mp3",
    "Avada Kedavra": "avadakedavra.mp3"
}

spell = input("Cast your spell: ")

if spell in spells:
    print(f"You cast {spell}! ✨")
    playsound(f"C:\\Users\\HP\\Desktop\\triwizard\\Task-9(playsound)\\{spells[spell]}")
else:
    print("Unknown spell!")
