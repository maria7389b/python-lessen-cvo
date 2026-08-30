# les01_extra_rapport.py

# Gegevens opvragen
servernaam = input("Servernaam: ")
ip_adres = input("IP-adres: ")
totaal_ram = float(input("Totaal RAM in GB: "))
gebruikt_ram = float(input("Gebruikt RAM in GB: "))
totale_schijf = float(input("Totale schijfruimte in GB: "))
gebruikte_schijf = float(input("Gebruikte schijfruimte in GB: "))
besturingssysteem = input("Besturingssysteem: ")
uptime = float(input("Uptime in dagen: "))
naam = input("Naam: ")

# Berekeningen
vrij_ram = totaal_ram - gebruikt_ram
percentage_ram = (gebruikt_ram / totaal_ram) * 100

vrije_schijf = totale_schijf - gebruikte_schijf
percentage_schijf = (gebruikte_schijf / totale_schijf) * 100

# Status RAM
if percentage_ram > 85:
    status_ram = "KRITIEK ⚠"
elif percentage_ram > 60:
    status_ram = "HOOG"
else:
    status_ram = "OK ✓"

# Status schijfruimte
if percentage_schijf > 90:
    status_schijf = "KRITIEK ⚠"
elif percentage_schijf > 70:
    status_schijf = "HOOG"
else:
    status_schijf = "OK ✓"


vrije_schijf = totale_schijf - gebruikte_schijf
percentage_schijf = (gebruikte_schijf / totale_schijf) * 100

# Rapport
balk_gelijk = "=" * 55
balk_min = "-" * 55
titel = "SYSTEEMRAPPORT – CVO Vitant Monitoring"

print()
print(balk_gelijk)
print(titel.center(55))
print(balk_gelijk)

print(">> SERVER-INFO")
print(f"   {'Servernaam':<11}: {servernaam}")
print(f"   {'IP-adres':<11}: {ip_adres}")
print(f"   {'OS':<11}: {besturingssysteem}")
print(f"   {'Uptime':<11}: {uptime:.1f} dagen")

print()
print(">> GEHEUGEN (RAM)")
print(f"   {'Totaal':<11}: {totaal_ram:.1f} GB")
print(f"   {'Gebruikt':<11}: {gebruikt_ram:.1f} GB  ({percentage_ram:.1f}%)  [{status_ram}]")
print(f"   {'Vrij':<11}: {vrij_ram:.1f} GB")

print()
print(">> SCHIJFRUIMTE")
print(f"   {'Totaal':<11}: {totale_schijf:.1f} GB")
print(f"   {'Gebruikt':<11}: {gebruikte_schijf:.1f} GB  ({percentage_schijf:.1f}%)  [{status_schijf}]")
print(f"   {'Vrij':<11}: {vrije_schijf:.1f} GB")

print()
print(balk_min)
print(f"Rapport gegenereerd door: {naam}")
print(balk_min)

