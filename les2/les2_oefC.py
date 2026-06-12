getal1 = int(input("Geef het eerste getal:"))
getal2 = int(input("Geef het tweede getal:"))

som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2

print("som:", som)
print("verschil:", verschil)
print("prodoct:", product)
print("deling:", deling)

#even of oneven
if getal1 % 2 == 0:
    print("Even")
else:
    print("oneven")

# kwadraat
kwadraat = getal1 ** 2
print("kwadraat:", kwadraat)
