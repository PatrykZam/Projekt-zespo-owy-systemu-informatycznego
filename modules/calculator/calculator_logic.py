
def przelicz_wartosci(kcal, bialko, tluszcze, weglowodany, ilosc, jednostka):
    # Zamiana kilogramow na gramy i litrow na mililitry
    if jednostka in ["kg", "l"]:
        ilosc_podstawowa = ilosc * 1000
    else:
        ilosc_podstawowa = ilosc

    # Wartosc na etykiecie dotyczy 100 g lub 100 ml
    mnoznik = ilosc_podstawowa / 100

    wyniki = {
        "kcal": round(kcal * mnoznik, 2),
        "bialko": round(bialko * mnoznik, 2),
        "tluszcze": round(tluszcze * mnoznik, 2),
        "weglowodany": round(weglowodany * mnoznik, 2)
    }

    return wyniki
