from datetime import date

def aktueller_monat_und_jahreszeit():
    monate = {
        1: "Januar",
        2: "Februar",
        3: "März",
        4: "April",
        5: "Mai",
        6: "Juni",
        7: "Juli",
        8: "August",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Dezember"
    }

    monat = date.today().month

    # Jahreszeit wie bisher
    if monat in (3, 4, 5):
        jahreszeit = "Frühling"
    elif monat in (6, 7, 8):
        jahreszeit = "Sommer"
    elif monat in (9, 10, 11):
        jahreszeit = "Herbst"
    else:
        jahreszeit = "Winter"

    return {
        "monat": monate[monat],
        "jahreszeit": jahreszeit
    }
