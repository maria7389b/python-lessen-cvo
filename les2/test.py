import tkinter as tk
root = tk .TK()
root.mainloop()
producten = ['Brood', 'Melk', 'Kaas', 'Boter']
resultaat = []

for p in producten:
    if len(p) > 4:
        resultaat.append(p.upper())
