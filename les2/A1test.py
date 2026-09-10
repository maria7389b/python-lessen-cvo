a = '25'
b = 4.0
c = True
print(int('25') + 10)
leeftijd = int(input('Wat is je leeftijd? '))

if leeftijd > 18:
    print('Meerderjarig')
cijfer = int(input('Geef een cijfer: '))

if cijfer < 0 or cijfer > 20:
    print('Ongeldige invoer')
elif cijfer >= 16:
    print('Uitmuntend')
elif cijfer >= 14:
    print('Zeer goed')
elif cijfer >= 10:
    print('Voldoende')
else:
    print('Onvoldoende')
wachtwoord = input('Geef een wachtwoord: ')

while len(wachtwoord) < 8:
    print('Te kort, probeer opnieuw.')
    wachtwoord = input('Geef een wachtwoord: ')

print('Wachtwoord geaccepteerd.')
prijzen = [12.50, 8.75, 24.00, 5.30, 19.99]

totaal = 0
for prijs in prijzen:
    totaal += prijs
print(totaal)

for prijs in prijzen:
    if prijs > 10:
        print(prijs)

prijzen.append(15.00)
print(prijzen)
def bereken_gemiddelde(lijst):
    totaal = 0
    for c in lijst:
        totaal += c
    return totaal / len(lijst)

print(bereken_gemiddelde([14, 16, 12, 18, 15]))
print(bereken_gemiddelde([10, 12, 14]))
def voeg_toe(totaal, bedrag):
    totaal = totaal + bedrag
    return totaal

print(voeg_toe(0, 10))
class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.km_stand = 0

    def rij(self, km):
        if km > 0:
            self.km_stand += km

    def __str__(self):
        return f'{self.merk} {self.model} ({self.bouwjaar}) | {self.km_stand} km'


auto1 = Voertuig('BMW', '3 Serie', 2020)
auto2 = Voertuig('Audi', 'A4', 2022)

auto1.rij(100)
auto2.rij(50)

print(auto1)
print(auto2)



class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.km_stand = 0

    def rij(self, km):
        if km > 0:
            self.km_stand += km
            return True
        return False

    def __str__(self):
        return f'{self.merk} {self.model} ({self.bouwjaar}) | {self.km_stand} km'


voertuigen = []

def voeg_voertuig_toe(lijst):
    merk = input('Merk: ')
    model = input('Model: ')
    bouwjaar = int(input('Bouwjaar: '))

    if bouwjaar >= 1990 and bouwjaar <= 2026:
        lijst.append(Voertuig(merk, model, bouwjaar))
        print('Voertuig toegevoegd!')
    else:
        print('Ongeldig bouwjaar.')

def voeg_km_toe(lijst):
    if len(lijst) == 0:
        print('Er zijn nog geen voertuigen.')
        return

    print('Voertuigen:')
    for i, voertuig in enumerate(lijst):
        print(i + 1, voertuig)

    keuze = int(input('Welk voertuig wil je aanpassen? '))

    if keuze >= 1 and keuze <= len(lijst):
        km = int(input('Hoeveel km toevoegen? '))

        if km > 0:
            lijst[keuze - 1].rij(km)
            print('Kilometers toegevoegd!')
        else:
            print('Kilometers moeten groter zijn dan 0.')
    else:
        print('Ongeldig volgnummer.')


def toon_overzicht(lijst):
    if len(lijst) == 0:
        print('Er zijn nog geen voertuigen.')
    else:
        for voertuig in lijst:
            print(voertuig)


actief = True

while actief:
    print()
    print('1) Voertuig toevoegen')
    print('2) Kilometers toevoegen')
    print('3) Overzicht tonen')
    print('4) Stop')

    keuze = input('Keuze: ')

    if keuze == '1':
        voeg_voertuig_toe(voertuigen)
    elif keuze == '2':
        voeg_km_toe(voertuigen)
    elif keuze == '3':
        toon_overzicht(voertuigen)
    elif keuze == '4':
        actief = False
        print('Programma gestopt.')
    else:
        print('Ongeldige keuze.')

class ElektrischeWagen(Voertuig):
    def __init__(self, merk, model, bouwjaar):
        super().__init__(merk, model, bouwjaar)
        self.laadniveau = 100

    def laad(self, procent):
        self.laadniveau += procent

        if self.laadniveau > 100:
            self.laadniveau = 100

    def __str__(self):
        return f'{self.merk} {self.model} ({self.bouwjaar}) | {self.km_stand} km | Batterij: {self.laadniveau}%'



