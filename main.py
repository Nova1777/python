import random

woordenlijst = [
    "informatica", "informatiekunde", "spelletje", "aardigheidje",
    "scholier", "fotografie", "waardebepaling", "specialiteit",
    "verzekering", "universiteit", "heesterperk"
]

def kies_woord():
    return random.choice(woordenlijst)

def speel_spel():
    woord = kies_woord()
    geraden = ["-"] * len(woord)
    fouten = []
    beurten = 5

    print(f"\nNieuw spel gestart. Het woord heeft {len(woord)} letters. Je hebt {beurten} beurten.\n")

    while beurten > 0 and "".join(geraden) != woord:
        print("Woord:", "".join(geraden))
        if fouten:
            print("Foute letters:", ", ".join(sorted(fouten)))

        letter = input("Voer een letter in: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Invoer klopt niet alleen 1 letter per beurt.")
            beurten -= 1
        elif letter in woord:
            for i, l in enumerate(woord):
                if l == letter:
                    geraden[i] = letter
            print("letter zit er in\n")
        elif letter not in fouten:
            fouten.append(letter)
            beurten -= 1
            print("Fout\n")
        else:
            print("Deze letter had je al fout geraden.")

        print(f"Nog {beurten} beurten.\n")

    if "".join(geraden) == woord:
        print(f" VICTORY '{woord}' geraden.\n")
    else:
        print(f"YOU LOST. Het woord was '{woord}'.\n")

def start_spel():
    while True:
        speel_spel()
        if input("Nog een spel (ja/nee): ").strip().lower() != "ja":
            print("Bedankt voor het spelen")
            break

start_spel()

