import tkinter as tk
from tkinter import messagebox
from hb_modul import HBKoltsegkezelo

app = tk.Tk()
app.title("Költségnyilvántartó HB")
app.geometry("400x500")
kezelo = HBKoltsegkezelo()
tk.Label(app, text="Tétel neve:").pack(pady=5)
nev_entry = tk.Entry(app, width=30)
nev_entry.pack()
tk.Label(app, text="Összeg (Ft):").pack(pady=5)
osszeg_entry = tk.Entry(app, width=30)
osszeg_entry.pack()
tipus_var = tk.StringVar(value="Kiadás")
tk.Radiobutton(app, text="Kiadás", variable=tipus_var, value="Kiadás").pack()
tk.Radiobutton(app, text="Bevétel", variable=tipus_var, value="Bevétel").pack()
lista_box = tk.Listbox(app, width=45, height=10)
lista_box.pack(pady=10)
egyenleg_label = tk.Label(app, text="Egyenleg: 0 Ft", font=("Arial", 12, "bold"))
egyenleg_label.pack(pady=10)
def hozzaadas():
    nev = nev_entry.get().strip()
    if nev == "":
        messagebox.showwarning("Hiányzó adat", "Add meg a tétel nevét!")
        return
    try:
        osszeg = int(osszeg_entry.get())
    except ValueError:
        messagebox.showerror("Hiba", "Az összegnek számnak kell lennie!")
        return
    tipus = tipus_var.get()
    kezelo.uj_tetel(tipus, nev, osszeg)
    lista_box.insert(tk.END, f"{tipus}: {nev} - {osszeg} Ft")
    egyenleg = kezelo.osszegzes()
    egyenleg_label.config(text=f"Egyenleg: {egyenleg} Ft")
    nev_entry.delete(0, tk.END)
    osszeg_entry.delete(0, tk.END)
    tetelszam = len(kezelo.tetelek)
    if tetelszam == 10:
        fajlnev = kezelo.hb_mentes_csv()
        messagebox.showinfo(
            "Automatikus mentés",
            f"Elérted a {tetelszam} tételt.\nAdatok autómatikusan elmentve ide:\n{fajlnev}"
        )
def mentes():
    fajlnev = kezelo.hb_mentes_csv()
    messagebox.showinfo("Mentés", f"Adatok manuálisan elmentve ide:\n{fajlnev}")
tk.Button(app, text="Hozzáadás", command=hozzaadas).pack(pady=5)
tk.Button(app, text="Manuális mentés", command=mentes).pack(pady=5)
tk.Label(app, text="(Automatikus mentés minden 10. tétel után)", fg="gray").pack(pady=3)

app.mainloop()
