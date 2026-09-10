import tkinter as tk
from tkinter import messagebox




def is_geldig_bouwjaar(jaar):
    return jaar >= 1990 and jaar <= 2026


voertuigen = []


def voertuig_toevoegen():
    merk = merk_entry.get()
    model = model_entry.get()
    bouwjaar_tekst = bouwjaar_entry.get()

    try:
        bouwjaar = int(bouwjaar_tekst)
    except ValueError:
        messagebox.showerror('Fout', 'Bouwjaar moet een getal zijn!')
        return

    if is_geldig_bouwjaar(bouwjaar):
        tekst = f'{merk} {model} ({bouwjaar})'
        voertuigen.append(tekst)
        overzicht.insert(tk.END, tekst)
        messagebox.showinfo('Gelukt', 'Voertuig toegevoegd!')
    else:
        messagebox.showerror('Fout', 'Ongeldig bouwjaar!')


def wis_velden():
    merk_entry.delete(0, tk.END)
    model_entry.delete(0, tk.END)
    bouwjaar_entry.delete(0, tk.END)


venster = tk.Tk()
venster.title('AutoTrack NV - Voertuigbeheer')
venster.geometry('500x400')



tk.Label(venster, text='Voertuigbeheersysteem').grid(
    row=0, column=0, columnspan=2, pady=10
)

tk.Label(venster, text='Merk:').grid(row=1, column=0)
merk_entry = tk.Entry(venster)
merk_entry.grid(row=1, column=1)

tk.Label(venster, text='Model:').grid(row=2, column=0)
model_entry = tk.Entry(venster)
model_entry.grid(row=2, column=1)

tk.Label(venster, text='Bouwjaar:').grid(row=3, column=0)
bouwjaar_entry = tk.Entry(venster)
bouwjaar_entry.grid(row=3, column=1)


tk.Button(
    venster,
    text='Voertuig toevoegen',
    command=voertuig_toevoegen
).grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(
    venster,
    text='Wis velden',
    command=wis_velden
).grid(row=5, column=0, columnspan=2)


overzicht = tk.Listbox(venster, width=50)
overzicht.grid(row=6, column=0, columnspan=2, pady=10)


venster.mainloop()


