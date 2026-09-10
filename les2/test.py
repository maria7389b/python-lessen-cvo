
class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.km_stand = 0


v1 = Voertuig('Volvo', 'FH16', 2023)

print(v1.merk)
print(v1.km_stand)
print(v1)
v1 = Voertuig('Volvo', 'FH16', 2023)

v2 = Voertuig('Mercedes', 'Actros', 2021)

v2.km_stand = 45000

print(v1.km_stand)
print(v2.km_stand)


class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.km_stand = 0

    # C1 – Methode rij()
    def rij(self, km):
        if km > 0:
            self.km_stand += km
        else:
            print("Ongeldige kilometerstand: km moet positief zijn.")

    # C2 – Methode __str__()
    def __str__(self):
        return f'{self.merk} {self.model} (bouwjaar {self.bouwjaar}) | {self.km_stand} km'

v1 = Voertuig('Volvo', 'FH16', 2023)

v1.rij(250)
v1.rij(-10)
v1.rij(100)

print(v1.km_stand)
v2 = Voertuig('Volvo', 'FH16', 2023)

v2.rij(350)

print(v2)
class Fiets:
    def __init__(self, merk, versnellingen):
        self.merk = merk
        self.versnellingen = versnellingen


f1 = Fiets('Trek', 21)

print(f1.merk)

vloot = []

print("=== Voertuigenregister AutoTrack NV ===")

while True:
    merk = input('Merk (of "q"): ')

    if merk.lower() == "q":
        break

    model = input("Model: ")
    bouwjaar = int(input("Bouwjaar: "))

    voertuig = Voertuig(merk, model, bouwjaar)
    vloot.append(voertuig)

print("\n--- Voertuigenregister AutoTrack NV ---")

for voertuig in vloot:
    print(voertuig)
    print("\n--- Kilometers toevoegen ---")

while True:
    if len(vloot) == 0:
        print("De vloot is leeg.")
        break

    print("\nVoertuigen:")

    for i, voertuig in enumerate(vloot, 1):
        print(f"{i}. {voertuig}")

    keuze = int(input("Voertuignummer (0 = stoppen): "))

    if keuze == 0:
        break

    if keuze < 1 or keuze > len(vloot):
        print("Ongeldig voertuignummer.")
        continue

    km = int(input("Aantal kilometers: "))

    vloot[keuze - 1].rij(km)

print("\n--- Finaal overzicht ---")

for voertuig in vloot:
    print(voertuig)
print("\n--- Test ElektrischeWagen ---")

elektrisch = ElektrischeWagen("Tesla", "Model 3", 2024, 75)

elektrisch.rij(100)

print(elektrisch)

elektrisch.laad(-20)

print(elektrisch)

elektrisch.laad(50)

print(elektrisch)
class ElektrischeWagen(Voertuig):
    def __init__(self, merk, model, bouwjaar, batterij_kwh):
        super().__init__(merk, model, bouwjaar)
        self.batterij_kwh = batterij_kwh
        self.laadniveau = 100

    def laad(self, procent):
        self.laadniveau += procent

        if self.laadniveau > 100:
            self.laadniveau = 100

    def __str__(self):
        return f"{self.merk} {self.model} (bouwjaar {self.bouwjaar}) | {self.km_stand} km | Batterij: {self.laadniveau}%"