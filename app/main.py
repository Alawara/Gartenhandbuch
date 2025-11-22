from fastapi import FastAPI

from .wetter import hol_wetter

from .jahreszeiten import aktuelle_jahreszeit

app = FastAPI(title="Gartenhandbuch")



@app.get("/")
def read_root():
    wetterdaten = hol_wetter()

    for item in wetterdaten:
        print(item) 

    
    
    return {
        "message": "Du hast dein Gartenhandbuch geöffnet!!",
        "So ist das Wetter heute!": wetterdaten ,
        "Jahreszeit": jahreszeit(),
        "Aufgaben": garten_aufgaben
        }


import json

garten_datei = open("app/gartenarbeiten.json", "r", encoding="utf-8")
garten_aufgaben = json.load(garten_datei)

garten_datei.close()

    
@app.get("/aufgaben")
def get_aufgaben():
    return garten_aufgaben

@app.get("/wetter")
def wetter():
    # ruft die Funktion in wetter.py auf
    wetterdaten = hol_wetter()
    return wetterdaten

@app.get("/jahreszeiten")
def jahreszeit():
    saison = aktuelle_jahreszeit()
    return saison

