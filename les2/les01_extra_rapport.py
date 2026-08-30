servernaam = input("Servernaam: ")
ip_adres = input("IP-adres: ")

totaal_ram = float(input("Totaal RAM in GB: "))
gebruikt_ram = float(input("Gebruikt RAM in GB: "))

totale_schijf = float(input("Totale schijfruimte in GB: "))
gebruikte_schijf = float(input("Gebruikte schijfruimte in GB: "))

besturingssysteem = input("Besturingssysteem: ")
uptime = float(input("Uptime in dagen: "))

vrij_ram = totaal_ram - gebruikt_ram
percentage_ram = (gebruikt_ram / totaal_ram) * 100

vrije_schijfruimte = totale_schijf - gebruikte_schijf
percentage_schijf = (gebruikte_schijf / totale_schijf) * 100

print("=" * 55)
print("  SYSTEEMRAPPORT – CVO Vitant Monitoring".center(55))
print("=" * 55)

print(">> SERVER-INFO")
print(f"   Servernaam : {servernaam}")
print(f"   IP-adres   : {ip_adres}")
print(f"   OS         : {besturingssysteem}")
print(f"   Uptime     : {uptime:.1f} dagen")
print()

print(">> GEHEUGEN (RAM)")
print(f"   Totaal     : {totaal_ram:.1f} GB")
print(f"   Gebruikt   : {gebruikt_ram:.1f} GB  ({percentage_ram:.1f}%)")
print(f"   Vrij       : {vrij_ram:.1f} GB")
print()

print(">> SCHIJFRUIMTE")
print(f"   Totaal     : {totale_schijf:.1f} GB")
print(f"   Gebruikt   : {gebruikte_schijf:.1f} GB  ({percentage_schijf:.1f}%)")
print(f"   Vrij       : {vrije_schijfruimte:.1f} GB")
print()

print("-" * 55)
print("Rapport gegenereerd door: Sam")
print("-" * 55)
