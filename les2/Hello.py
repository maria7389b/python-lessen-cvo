print('Hello, Worlod!')
teller = 1

while teller <= 8: 
    print(teller)
    teller = teller + 1

teller = 7

while teller >= 0:
    print(teller)
    teller = teller - 1

print('Boem!')

som = 0
teller = 1

while teller <= 49:
    if teller % 2 != 0:
        som = som + teller
    teller = teller + 1

print('De som van alle oneven getallen t/m 49 is:', som)

# B4
som = 0
teller = 1

while teller <= 49:
    if teller % 2 != 0:
        som = som + teller
    teller = teller + 1

print('De som van alle oneven getallen t/m 49 is:', som)

temperatuur = int(input('Temperatuur in graden Celsius: '))

while temperatuur < -50 or temperatuur > 60:
    print('Ongeldige temperatuur, probeer opnieuw.')
    temperatuur = int(input('Temperatuur in graden Celsius: '))

print('Geldige temperatuur geregistreerd:', temperatuur, 'graden')

aantalProducten = 0

product = input('Productnaam (of "q" om te stoppen): ')

while product != 'q':
    aantalProducten = aantalProducten + 1
    product = input('Productnaam (of "q" om te stoppen): ')

print('Je hebt', aantalProducten, 'producten ingescand.')


aantalProducten = 0
totaal = 0

product = input('Productnaam (of "q" om te stoppen): ')

while product != 'q':
    prijs = float(input('Prijs: €'))

    aantalProducten = aantalProducten + 1
    totaal = totaal + prijs

    product = input('Productnaam (of "q" om te stoppen): ')

print('Je hebt', aantalProducten, 'producten ingescand.')
print(f'Totaal: €{totaal:.2f}')
-60
aantalProducten = 0
totaal = 0

product = input('Productnaam (of "q" om te stoppen): ')

while product != 'q':
    prijs = float(input('Prijs: €'))

    while prijs < 0 or prijs > 999.99:
        print('Ongeldige prijs. Voer een bedrag in tussen €0.00 en €999.99.')
        prijs = float(input('Prijs: €'))

    aantalProducten = aantalProducten + 1
    totaal = totaal + prijs

    product = input('Productnaam (of "q" om te stoppen): ')

print('Je hebt', aantalProducten, 'producten ingescand.')

if totaal > 100:
    kortingPercentage = 10
elif totaal > 50:
    kortingPercentage = 5
else:
    kortingPercentage = 0

korting = totaal * kortingPercentage / 100
teBetalen = totaal - korting

print(f'Totaal voor korting: €{totaal:.2f}')
print(f'Korting ({kortingPercentage}%): -€{korting:.2f}')
print(f'Te betalen: €{teBetalen:.2f}')
