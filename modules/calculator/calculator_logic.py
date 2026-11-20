
import math


def przelicz_wartosci(kcal, bialko, tluszcze, weglowodany, ilosc, jednostka):
    przeliczniki = {
        "g": 1,
        "kg": 1000,
        "ml": 1,
        "l": 1000
    }

    if jednostka not in przeliczniki:
        raise ValueError("Nieprawidłowa jednostka produktu.")

    dane = {
        "Kalorie": kcal,
        "Białko": bialko,
        "Tłuszcze": tluszcze,
        "Węglowodany": weglowodany,
        "Ilość": ilosc
    }

    for nazwa, wartosc in dane.items():
        try:
            liczba = float(wartosc)
        except (TypeError, ValueError):
            raise ValueError(f"{nazwa}: podaj poprawną liczbę.")

        if not math.isfinite(liczba):
            raise ValueError(f"{nazwa}: nieprawidłowa wartość.")

        if nazwa == "Ilość" and liczba <= 0:
            raise ValueError("Spożyta ilość musi być większa od zera.")

        if nazwa != "Ilość" and liczba < 0:
            raise ValueError(f"{nazwa}: wartość nie może być ujemna.")

    ilosc_podstawowa = ilosc * przeliczniki[jednostka]
    mnoznik = ilosc_podstawowa / 100

    return {
        "kcal": round(kcal * mnoznik, 2),
        "bialko": round(bialko * mnoznik, 2),
        "tluszcze": round(tluszcze * mnoznik, 2),
        "weglowodany": round(weglowodany * mnoznik, 2)
    }
