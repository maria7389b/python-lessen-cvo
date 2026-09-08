

producten = ['Brood', 'Melk', 'Kaas', 'Boter']
resultaat = []
for p in producten:
        if len(p) > 4:
            resultaat.append(p.upper())
print(resultaat)
print(len(resultaat))

        
def bereken_korting(prijs):
    korting = prijs * 0.15
    return prijs - korting
def pas_korting_toe(prijs, percentage):
        # jouw code hier

    pas_korting_toe(49.99, 10)
    pas_korting_toe(129.00, 10)
    pas_korting_toe(8.50, 10)


