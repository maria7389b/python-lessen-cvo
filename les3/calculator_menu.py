# geintegreerd_menu.py – gemaakt door [jouw naam]

while True:
    print("\n" + "=" * 45)
    print(" HOOFDMENU ERPM-SYSTEEM PRIMABOUW")
    print("=" * 45)
    print("1) BTW-Calculator (Les 3)")
    print("2) Kortingscalculator (Les 4)")
    print("3) Werf- & Stellingveiligheid (Les 4)")
    print("4) Applicatie afsluiten")
    print("=" * 45)

    keuze = input("Maak uw keuze (1-4): ")

    if keuze == "1":
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")

        bedrag = float(input("Geef bedrag in €: "))
        btw = float(input("Geef BTW percentage: "))

        btw_bedrag = bedrag * btw / 100
        totaal = bedrag + btw_bedrag

        print(f"BTW bedrag: €{btw_bedrag:.2f}")
        print(f"Totaal: €{totaal:.2f}")

    elif keuze == "2":
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")

        prijs = float(input("Geef prijs in €: "))
        korting = float(input("Geef korting %: "))

        korting_bedrag = prijs * korting / 100
        eindprijs = prijs - korting_bedrag

        print(f"Korting: €{korting_bedrag:.2f}")
        print(f"Eindprijs: €{eindprijs:.2f}")

    elif keuze == "3":
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")

        wind_kmh = float(input("Windsnelheid (km/u): "))
        kraan_hoogte = float(input("Kraanhoogte (m): "))

        if wind_kmh > 45 and kraan_hoogte > 20:
            print("❌ KRAAN STATUS: VERBODEN")
        elif wind_kmh > 55 or kraan_hoogte > 40:
            print("⚠️ KRAAN STATUS: UITERSTE VOORZICHTIGHEID")
        else:
            print("✅ KRAAN STATUS: NORMAAL")

    elif keuze == "4":
        print("\nBedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break

    else:
        print("❌ Ongeldige keuze! Voer 1-4 in.")