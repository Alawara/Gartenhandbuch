<<<<<<< HEAD
Gartenhandbuch



Idee: 



Eine Web-App, die mir abhängig von Wetter und Jahreszeit Empfehlungen für Gartenarbeiten, gibt beziehungsweise mich an anfallende Arbeiten erinnert. Dieses Projekt dient gleichzeitig als Übungsprojekt für meine Umschulung in Anwendungsentwicklung.





Bisher erreicht: 



Grundlegende Projektstruktur festgelegt, als besondere Herausforderung alles in der Kommandozeile gemacht um den Umgang mit Git und der Shell zu üben. (Je eine eigene Python-Datei für Wetter und Jahreszeit, sowie eine json-Datei um die bei mir im Garten anfallenden Arbeiten zu speichern), Requirements-Datei angelegt. 



Virtuelle Umgebung eingerichtet (wichtig für konfliktfreies Arbeiten mit installierten Modulen)



FastAPI-App erstellt



Ich kann auf http://127.0.0.1:8000/ eine Nachricht sehen, die App funktioniert so weit. 





Als nächstes habe ich geplant: 



Wetterdaten abrufen und anzeigen (über open-meteo API)



Jahreszeit erkennen (via datetime)



Gartenarbeiten kategorisieren und in json-Datei eintragen. 



Abhängig von Wetter und Jahreszeit Gartenarbeiten vorschlagen







Wichtige Schritte: 



Python 3.x



Virtuelle Umgebung erstellen:

&nbsp;  python -m venv venv



Aktivieren:

&nbsp;  venv\\Scripts\\activate  (Windows)

&nbsp;  source venv/bin/activate  (Linux/macOS)



Abhängigkeiten installieren:

&nbsp;  pip install -r requirements.txt



App starten:

&nbsp;  uvicorn app.main:app --reload



=======
# Gartenhandbuch
Gartenhandbuch ist ist eine kleine Web-Applikation, die unter Berücksichtigung der Jahreszeit und der aktuellen Wetterverhältnisse an anfallende Gartenarbeiten erinnert. Das Projekt dient als Übung im Umgang mit Python, Web-Frameworks und Git
>>>>>>> 4912a7666d1babd105b0d84aa49ce4d74d360c94
