class Sensor:
    def __init__(self, naam, waarde):
        self.naam = naam
        self.waarde = waarde

    def verhoog(self, stap):
        self.waarde += stap

    def __str__(self):
        return f'{self.naam}: {self.waarde}'


s1 = Sensor('Temp', 20)
s2 = Sensor('Druk', 100)

s1.verhoog(5)
s1.verhoog(-3)
s2.verhoog(10)

print(s1)
print(s2)
print(s1.waarde + s2.waarde)
