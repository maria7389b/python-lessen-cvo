from les_oop import Voertuig

vloot = []

# ── D5 – Voertuig-objecten toevoegen ──

while True:
    merk = input("Merk (of 'q' om te stoppen): ")

    if merk == "q":
        break

    model = input("Model: ")
    bouwjaar = int(input("Bouwjaar: "))

    voertuig = Voertuig(merk, model, bouwjaar)
    vloot.append(voertuig)


# ── Voertuigen tonen ──

print("--- Vlootoverzicht ---")

for v in vloot:
    print(v)


# ── Bonus: voertuigen vanaf 2020 ──

print("--- Voertuigen vanaf 2020 ---")

for v in vloot:
    if v.bouwjaar >= 2020:
        print(v)
