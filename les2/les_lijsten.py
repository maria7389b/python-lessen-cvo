vloot = []

while True:
    merk = input("Geef een merk (of 'q' om te stoppen): ")

    if merk == "q":
        break

    vloot.append(merk)

print(f"Er zijn {len(vloot)} voertuigen geregistreerd.")


te_verwijderen = input("Welk merk wil je verwijderen? ")

if te_verwijderen in vloot:
    vloot.remove(te_verwijderen)
    print(f"{te_verwijderen} is verwijderd.")
else:
    print("Dit merk staat niet in de vloot.")

print("--- Bijgewerkt vlootoverzicht ---")

for nummer, merk in enumerate(vloot, start=1):
    print(f"{nummer}. {merk}")
from les_oop import Voertuig

vloot = []



while True:
    merk = input("Merk (of 'q' om te stoppen): ")

    if merk == "q":
        break

    model = input("Model: ")
    bouwjaar = int(input("Bouwjaar: "))

    voertuig = Voertuig(merk, model, bouwjaar)
    vloot.append(voertuig)



print("--- Vlootoverzicht ---")

for v in vloot:
    print(v)



print("--- Voertuigen vanaf 2020 ---")

for v in vloot:
    if v.bouwjaar >= 2020:
        print(v)

