import csv
import os
from datetime import datetime
class HBKoltsegkezelo:
    def __init__(self):
        self.tetelek = []
    def uj_tetel(self, tipus, nev, osszeg):
        self.tetelek.append({
            "tipus": tipus,
            "nev": nev,
            "osszeg": osszeg})
    def osszegzes(self):
        bevetel = sum(t["osszeg"] for t in self.tetelek if t["tipus"] == "Bevétel")
        kiadas = sum(t["osszeg"] for t in self.tetelek if t["tipus"] == "Kiadás")
        return bevetel - kiadas
    def hb_mentes_csv(self):
        honap = datetime.now().strftime("%Y-%m")
        fajlnev = f"{honap}_koltsegek.csv"
        with open(fajlnev, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tipus", "nev", "osszeg"])
            writer.writeheader()
            writer.writerows(self.tetelek)
        return fajlnev