# offerte_check.py

winst = float(input("Geschatte winst (€): "))
personeel = int(input("Beschikbaar personeel: "))
risico = input("Risicofactor (Laag/Medium/Hoog): ")

if risico == "Hoog" and winst < 1000:
    print("❌ GEWEIGERD")
elif personeel < 5:
    print("⚠️ ON HOLD")
else:
    print("✅ GOEDGEKEURD")