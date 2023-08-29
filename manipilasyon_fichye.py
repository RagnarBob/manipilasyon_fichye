import re
import random


def li_fichye(chemen):
    try:
        with open(chemen, 'r') as fichye:
            kontni = fichye.read()
            return kontni
    except FileNotFoundError:
        return "Erè: Fichye a pa jwenn."

def afiche_teks(teks):
    print("Contents of the file:\n")
    print(teks)
   

def modifye_teks(teks, ajoute_teks="", endeks=None):
    if endeks is None:
        teks_modifye = teks + ajoute_teks
    else:
        teks_modifye = teks[:endeks] + ajoute_teks + teks[endeks:]
    return teks_modifye

def netwaye_teks(teks):
    teks_netwaye = teks.strip()
    teks_netwaye = re.sub(r'[^\w\s]', '', teks_netwaye)
    return teks_netwaye

def sove_teks(chemen, teks):
    with open(chemen, 'w') as fichye:
        fichye.write(teks)
    print("File saved successfully.")

print("Welcome to the Text File Editor!\n")

chemen = input("Enter the path to the text file: ")

while True:
    print("\n1. Read Text File")
    print("2. Display Text")
    print("3. Update Text")
    print("4. Clean Text")
    print("5. Save Text")
    print("6. Exit")
    
    chwa = input("\nPlease select an option: ")
    
    if chwa == "1":
        kontni = li_fichye(chemen)
    elif chwa == "2":
        afiche_teks(kontni)
    elif chwa == "3":
        ajoute_teks = input("Enter the new content (type 'done' on a new line to finish editing):\n")
        while ajoute_teks != "done":
            endeks = input("Enter an index to add the text (leave blank to append at the end): ")
            if endeks.isdigit():
                endeks = int(endeks)
                kontni = modifye_teks(kontni, ajoute_teks, endeks)
            else:
                kontni = modifye_teks(kontni, ajoute_teks)
            ajoute_teks = input()
    elif chwa == "4":
        kontni = netwaye_teks(kontni)
        print("Text cleaned successfully.")
    elif chwa == "5":
        sove_teks(chemen, kontni)
    elif chwa == "6":
        print("\nExiting the Text File Editor. Goodbye!")
        break
    else:
        print("Invalid option. Please select an available option.")