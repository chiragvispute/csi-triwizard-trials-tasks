import pyjokes

spell = input("Cast your spell: ")
if spell.lower() == "riddikulus":
    print(pyjokes.get_joke())
else:
    print("Nothing happened... Try again!")
