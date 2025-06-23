import random

woordenlijst = [
    "informatica", "informatiekunde", "spelletje", "aardigheidje",
    "scholier", "fotografie", "waardebepaling", "specialiteit",
    "verzekering", "universiteit", "heesterperk"
]

def kies_woord():
    return random.choice(woordenlijst)

def speel_spel():
    geheime_woord = kies_woord()
    geraden = "-" * len(geheime_woord)
    beurten = 5
    gebruikte_foute_letters = []

    print("\nNieuw spel gestart!")
    print(f"Het geheime woord heeft {len(geheime_woord)} letters.")
    print(f"Je hebt {beurten} beurten.\n")

    while beurten > 0 and geraden != geheime_woord:
        print("Huidige woord:", geraden)
        if gebruikte_foute_letters:
            print("Foute letters:", ", ".join(sorted(gebruikte_foute_letters)))
        letter = input("Voer een letter in: ").lower()

        # Inputcontrole: enkel één alfabetletter
        if len(letter) != 1 or not letter.isalpha():
            print("Ongeldige invoer! Voer slechts één letter in.")
            beurten -= 1
            print(f"Beurt verloren! Nog {beurten} beurten.\n")
            continue

        if letter in geheime_woord:
            nieuwe_geraden = ""
            for i in range(len(geheime_woord)):
                if geheime_woord[i] == letter:
                    nieuwe_geraden += letter
                else:
                    nieuwe_geraden += geraden[i]
            geraden = nieuwe_geraden
            print("Goede keuze!\n")
        else:
            if letter not in gebruikte_foute_letters:
                gebruikte_foute_letters.append(letter)
            beurten -= 1
            print(f"Fout! Nog {beurten} beurten over.\n")

    if geraden == geheime_woord:
        print(f" Gefeliciteerd! Je hebt het woord '{geheime_woord}' geraden.\n")
    else:
        print(f" Helaas, je hebt verloren. Het woord was '{geheime_woord}'.\n")

def start_spel():
    while True:
        speel_spel()
        opnieuw = input("Wil je nog een spel spelen? (ja/nee): ").lower()
        if opnieuw != "ja":
            print("Bedankt voor het spelen!")
            break

# Start het spel met herstart-optie
start_spel()