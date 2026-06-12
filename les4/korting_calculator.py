# korting_calculator.py – gemaakt door [Maria]
print("=" * 45)
print(" Korting Checker - PrimaBouw BV")
print("=" * 45)

totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))


if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000:
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0

# Berekeningen
kortingsbedrag = totaalbedrag * (korting_pct / 100)
eindbedrag = totaalbedrag - kortingsbedrag

print("-" * 45)
print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
print(f"Kortingspercentage: {korting_pct}%")
print(f"Kortingsbedrag    : €{kortingsbedrag:.2f}")
print(f"Netto te betalen  : €{eindbedrag:.2f}")
print("=" * 45)
# werf_veiligheid.py – gemaakt door Kris Dierickx
print("=" * 45)
print("     Veiligheids-Assistent PrimaBouw BV")
print("=" * 45)
wind_kmh = float(input("Wat is de actuele windsnelheid op de werf (km/u)? "))
if wind_kmh > 60:
    print("❌ CRITIEK GEVAAR: Stoppen met alle werkzaamheden! Evacueer de stellingen.")
elif wind_kmh > 30:
    # Genest niveau 1: De wind is matig tot krachtig. Status hangt af van veiligheidsnetten.
    netten = input("Zijn de verplichte veiligheidsnetten gemonteerd? (ja/nee): ")  
    if netten.lower() == "ja":
        print("⚠️ WAARSCHUWING: Werken toegestaan, maar wees alert op rukwinden.")
    else:
        print("❌ GEVAAR: Werken op hoogte VERBODEN zonder gemonteerde netten!")
else:
    # Genest niveau 2: Veilige wind, maar hoe zit het met neerslag?
    regen = input("Is er sprake van hevige regen of ijzel? (ja/nee): ")
    
    if regen.lower() == "ja":
        print("⚠️ WAARSCHUWING: Risico op gladheid. Werken toegestaan met antislip-schoeisel.")
    else:
        print("✅ VEILIG: Normale werkomstandigheden op de stellingen.")
print("\n--- EXTRA CONTROLE TORENKRAAN ---")
kraan_hoogte = float(input("Hoe hoog staat de kraanmast (in meters)? "))
wind_kmh = float(input("Hoe hard waait het (km/u)? "))

# Combineren met 'and' en 'or'
if wind_kmh > 45 and kraan_hoogte > 20:
    print("❌ KRAAN STATUS: Bediening VERBODEN wegens hefboomwind op grote hoogte.")
elif wind_kmh > 55 or kraan_hoogte > 40:
    print("⚠️ KRAAN STATUS: Alleen bediening door gecertificeerde masters. Wees uiterst voorzichtig.")
else:
    print("✅ KRAAN STATUS: Werking binnen de normale veiligheidsmarges.")