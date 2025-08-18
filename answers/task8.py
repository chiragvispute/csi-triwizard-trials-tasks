import emoji  

house_emojis = {
    "Gryffindor": ":lion:",
    "Slytherin": ":snake:",
    "Ravenclaw": ":eagle:",
    "Hufflepuff": ":badger:"
}

house = input("Enter a Hogwarts House: ")

if house in house_emojis:
    print(house, emoji.emojize(house_emojis[house]))
else:
    print("Unknown house! Try again.")
