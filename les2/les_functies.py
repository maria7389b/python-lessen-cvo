class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def __str__(self):
        return f"{self.merk} {self.model} ({self.bouwjaar})"


class Sensor:
    def __init__(self, naam, waarde):
            self.naam   = naam
            self.waarde = waarde
    def verhoog(self, stap):
            self.waarde += stap
    def __str__(self):
         return f'{self.naam}: {self.waarde}'

s1 = Sensor('Temp', 20)
s2 = Sensor('Druk', 100)
s1.verhoog(5)
s1.verhoog(-3)
s2.verhoog(10)
print(s1)
print(s2)
print(s1.waarde + s2.waarde)

def toon_banner():
    print("==============================")
    print("  AutoTrack NV – Vlootbeheer")
    print("==============================")


toon_banner()
toon_banner()
def begroet(naam):
    print(f"Goedemorgen, {naam}! Klaar voor de les?")


def toon_merk(merk, bouwjaar):
    print(f"{merk} (bouwjaar: {bouwjaar})")


def herhaal_lijn(teken, aantal):
    print(teken * aantal)


begroet("Jonas")
begroet("Sofie")

toon_merk("Volvo", 2023)
toon_merk("BMW", 2024)

herhaal_lijn("-", 20)
herhaal_lijn("*", 10)
def pas_korting_toe(prijs, percentage):
    korting = prijs * percentage / 100
    eindprijs = prijs - korting
    print(f"Na korting: {eindprijs:.2f}")


pas_korting_toe(49.99, 10)
pas_korting_toe(129.00, 10)
pas_korting_toe(8.50, 10)
def begroet_merk(merk, label="Voertuig"):
    print(f"Geregistreerd: {label} – {merk}")


begroet_merk("Volvo")
begroet_merk("FH16", "Truck")
begroet_merk("GLC 300", "SUV")

def kwadraat_print(n):
    print(n ** 2)
    return (n ** 2)
def kwadraat_return(n):
    return n ** 2

a = kwadraat_print(4)
b = kwadraat_return(4)
print(a)
print(b)
print(a + 1)
def bereken_btw(prijs, btw_pct=21):
    return prijs * btw_pct / 100


def eindprijs(prijs, btw_pct=21):
    btw = bereken_btw(prijs, btw_pct)
    return prijs + btw


def bereken_korting(prijs, pct):
    return prijs - (prijs * pct / 100)


# Testen
print(bereken_btw(100))
print(bereken_btw(50, 6))

print(eindprijs(100))

print(bereken_korting(100, 10))
def is_geldig_bouwjaar(jaar):
    return 1900 <= jaar <= 2026


def is_geldige_prijs(prijs):
    return 0 < prijs <= 999999


def is_beschikbaar(voorraad):
    return voorraad > 0


jaar = 2023
p = 25000
voorraad = 5

if is_geldig_bouwjaar(jaar) and is_geldige_prijs(p):
    print('Voertuig aanvaard')
else:
    print('Ongeldige gegevens')


def toon_vloot(vloot):
    if len(vloot) == 0:
        print("De vloot is momenteel leeg.")
    else:
        for i, merk in enumerate(vloot, 1):
            print(f"{i}. {merk}")
toon_vloot([])

toon_vloot(["Volvo", "BMW", "Scania"])