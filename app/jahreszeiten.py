from datetime import date

def aktuelle_jahreszeit():
    monat = date.today().month

    if monat in (3, 4, 5):
        return "Frühling"
    elif monat in (6, 7, 8):
        return "Sommer"
    elif monat in (9, 10, 11):
        return "Herbst"
    else:
        return "Winter"
