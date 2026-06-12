naam = input("Naam van de klant:")
aantal = int(input("Aantal producten:"))
prijs = float(input("prijs per stuk:"))

subtotaal = aantal * prijs
btw = subtotaal * 0.21
totaal = subtotaal + btw

print("======================================")
print("Factuur voor:", naam)
print("aantal producten:", aantal)
print("prijs per stuk: €", prijs)
print("--------------------------------------")
print("subtotaal:   €", subtotaal)
print("Btw (21%):   €", btw)
print("Totaal:      €", totaal)
print("======================================")

naam = input("Naam van de klant: ")
aantal = int(input("Aantal producten: "))

if aantal < 0:
    print("Fout: aantal producten mag niet negatief zijn")
else:
    prijs = float(input("Prijs per stuk: "))
    btw_percentage = float(input("BTW percentage (6, 12 of 21): "))

    subtotaal = aantal * prijs
    btw = subtotaal * (btw_percentage / 100)
    totaal = subtotaal + btw

    subtotaal = round(subtotaal, 2)
    btw = round(btw, 2)
    totaal = round(totaal, 2)

    print("===============================")
    print("Factuur voor:", naam)
    print("Aantal producten:", aantal)
    print("Prijs per stuk: €", prijs)
    print("-------------------------------")
    print("Subtotaal:      €", subtotaal)
    print("BTW:", btw_percentage, "%   €", btw)
    print("TOTAAL:         €", totaal)
    print("===============================")