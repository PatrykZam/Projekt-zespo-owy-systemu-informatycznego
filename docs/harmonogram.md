# 📅 CalorieTracker – Harmonogram i Kamienie Milowe

**Planowany termin ukończenia projektu:** 22 stycznia 2027 r.  
**Stos technologiczny:** Python, Streamlit, SQLite  
**Zespół:** 4 osoby  

---

## Kamienie Milowe (Milestones)

### M1: Przygotowanie środowiska, architektura i makiety UI
- **Termin:** do 15.11.2026
- **Zakres prac:**
  - Konfiguracja repozytorium GitHub (Issues, Projects/Kanban, zasady gałęzi).
  - Podział projektu na 4 moduły programistyczne (RNF-13) i przygotowanie struktury plików.
  - Zaprojektowanie schematu bazy danych SQLite dla kont, dzienników i celów (RF-12).
  - Przygotowanie makiet interfejsu w Streamlit z uwzględnieniem responsywności mobile/desktop (RNF-03).

---

### M2: Moduł Autoryzacji i Bazy Danych (Baza & Konta)
- **Termin:** do 06.12.2026
- **Zakres prac:**
  - Implementacja bazy danych SQLite, tworzenie tabel oraz modułu dostępu do danych (RF-12).
  - Rejestracja i logowanie użytkowników (RF-01, RF-02).
  - Bezpieczne przechowywanie haseł z użyciem hashowania (RNF-09).
  - Izolacja danych – przypisanie wpisów do konkretnego zalogowanego użytkownika (RF-13).

---

### M3: Kalkulator wartości odżywczych i Dziennik żywieniowy
- **Termin:** do 20.12.2026
- **Zakres prac:**
  - Formularz wprowadzania wartości odżywczych z etykiety na 100g/100ml (RF-03).
  - Przeliczanie kalorii i makro (B/T/W) na dowolną porcję w g/kg/ml/l wraz z walidacją (RF-04, RF-05, RNF-10, RNF-11).
  - Dodawanie przeliczonych produktów do dziennika z wybraną datą (RF-06).
  - Przeglądanie, edycja i usuwanie wpisów z wybranego dnia (RF-07).

---

### M4: Cele żywieniowe, Historia i Statystyki
- **Termin:** do 10.01.2027
- **Zakres prac:**
  - Ustawianie i edycja dziennych celów kalorycznych oraz makroskładników (RF-09).
  - Wyświetlanie sumy dziennej oraz paska postępu realizacji celów (RF-08, RF-10).
  - Przeglądanie historii spożycia z poprzednich dni (RF-11).
  - Dostosowanie widoków pod przeglądarki mobilne w sieci lokalnej (RNF-04, RNF-06).

---

### M5: Testy, Refaktoryzacja, Dokumentacja & Finalny Odbiór
- **Termin:** do 22.01.2027
- **Zakres prac:**
  - Testowanie poprawności przeliczeń i działania aplikacji offline / w sieci lokalnej (RNF-02, RNF-12).
  - Ostateczna weryfikacja i spięcie 4 modułów programistycznych w całość.
  - Przygotowanie dokumentacji końcowej w repozytorium oraz weryfikacja wkładu zespołu na GitHubie.
  - Finalna prezentacja i oddanie projektu (22.01.2027).

---

## 👥 Podział Modułów i Odpowiedzialności w Zespole

| Osoba | Moduł programistyczny | Zakres odpowiedzialności |
| :--- | :--- | :--- |
| **Członek 1** | Moduł Użytkowników i Autoryzacji | Rejestracja, logowanie, bezpieczne hashowanie haseł, obsługa sesji Streamlit (RF-01, RF-02, RNF-09, RF-13). |
| **Członek 2** | Moduł Bazy Danych i Warstwy Danych | Projekt bazy SQLite, zapytania SQL, operacje CRUD na dzienniku, celach i wpisach (RF-12, RF-07). |
| **Członek 3** | Moduł Kalkulatora i Logiki Przeliczeń | Przeliczanie jednostek g/kg/ml/l, walidacja poprawności danych i blokada wartości ujemnych (RF-03, RF-04, RF-05, RNF-10, RNF-11). |
| **Członek 4** | Moduł Dziennika, Celów i UI/UX | Podsumowania dzienne, wskaźniki postępu, historia spożycia, responsywność UI mobile/desktop (RF-06, RF-08, RF-09, RF-10, RF-11, RNF-03). |
