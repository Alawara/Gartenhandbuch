<<<<<<< HEAD
Gartenhandbuch



Idee: 



Eine Web-App, die mir abhängig von Wetter und Jahreszeit Empfehlungen für Gartenarbeiten, gibt beziehungsweise mich an anfallende Arbeiten erinnert. Dieses Projekt dient gleichzeitig als Übungsprojekt für meine Umschulung in Anwendungsentwicklung.





Bisher erreicht: 



Grundlegende Projektstruktur festgelegt, als besondere Herausforderung alles in der Kommandozeile gemacht um den Umgang mit Git und der Shell zu üben. (Je eine eigene Python-Datei für Wetter und Jahreszeit, sowie eine json-Datei um die bei mir im Garten anfallenden Arbeiten zu speichern), Requirements-Datei angelegt. 



Virtuelle Umgebung eingerichtet (wichtig für konfliktfreies Arbeiten mit installierten Modulen)



FastAPI-App erstellt



Ich kann auf http://127.0.0.1:8000/ eine Nachricht sehen, die App funktioniert so weit. 




Ich kann Wetterdaten abrufen und anzeigen (über open-meteo API)



Ich kann Jahreszeit erkennen (via datetime)



Habe Gartenarbeiten kategorisiert und in json-Datei eingetragen. 

Wetterdaten und Jahreszeit werden auf der http://127.0.0.1:8000/ angezeigt


Abhängig von der Jahreszeit werden Gartenarbeiten vorgeschlagen

Als nächstes habe ich geplant: 

Gartenarbeiten sollen auch abhängig vom Wetter angezeigt werden (bei Regen kann ich nicht draußen arbeiten)

Statt nach Jahreszeiten soll nach Monaten unterschieden werden. (Blumenzwiebeln besser schon im September bestellen, je nach Wetter kann ich sie dann bis November in die Erde bringen)








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
