from fastapi import FastAPI

from .wetter import hol_wetter


app = FastAPI(title="Gartenhandbuch")



@app.get("/")
def read_root():
    
    return {
        "message": "Du hast dein Gartenhandbuch geöffnet!"
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

