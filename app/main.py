from fastapi import FastAPI

from .wetter import hol_wetter

from .jahreszeiten import aktueller_monat_und_jahreszeit

app = FastAPI(title="Gartenhandbuch")

# with open: Sauberer, Datei wird auch bei Unterbrechung des Codes geschlossen: 
import json

with open("app/gartenarbeiten.json", "r", encoding="utf-8") as garten_datei:
    garten_aufgaben = json.load(garten_datei)


# aktuellen Monat und Jahreszeit bestimmen
zeit = aktueller_monat_und_jahreszeit()
monat = zeit["monat"]
jahreszeit = zeit["jahreszeit"]

# Filtern nach Aufgaben für die aktuelle Jahreszeit
aufgaben_jetzt = [
    aufgabe for aufgabe in garten_aufgaben
    if aufgabe.get("monat") == monat
]



@app.get("/")
def read_root():
    wetterdaten = hol_wetter()

    for item in wetterdaten:
        print(item) 

    
    
    return {
        "message": "Du hast dein Gartenhandbuch geöffnet!",
        "So ist das Wetter heute!": wetterdaten ,
        "Jahreszeit": jahreszeit,
        "Monat": monat,
        "Aufgaben für diese Jahreszeit": aufgaben_jetzt,
       
        }

    

@app.get("/wetter")
def wetter():
    # ruft die Funktion in wetter.py auf
    wetterdaten = hol_wetter()
    return wetterdaten

@app.get("/jahreszeiten")
def jahreszeit():
    zeit = aktueller_monat_und_jahreszeit()
    return zeit

