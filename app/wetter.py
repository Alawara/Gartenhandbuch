import requests

def hol_wetter():
    # Verwendet wird API von open-meteo, hier im Beispiel für die Koordinaten von Berlin. Zu Beachten: Angabe der Zeitzone für korrekte Uhrzeit
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=52.52&longitude=13.41&current_weather=true&timezone=Europe%2FBerlin" 
    )

    
    antwort = requests.get(url)

    #  Antwort der API als Dictionary lesen
    daten = antwort.json()

    # Nur aktuelle Daten
    return daten["current_weather"]
