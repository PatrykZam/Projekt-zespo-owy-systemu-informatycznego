# ORG-03 – Zadania programistyczne (Dev Tasks) i Backlog

**Projekt:** CalorieTracker  
**Technologie:** Python, Streamlit, SQLite  
**Zespół:** 4 osoby  
**Planowany termin ukończenia:** 22 stycznia 2027 r.

## 1. Cel dokumentu

Celem dokumentu jest określenie podziału prac programistycznych w projekcie CalorieTracker.

Projekt został podzielony na cztery główne moduły (MOD-01–MOD-04), za które odpowiadają poszczególni członkowie zespołu.

Każdy moduł składa się z mniejszych zadań technicznych (Dev Tasks), które będą realizowane i monitorowane za pomocą GitHub Issues oraz Sub-issues.

## 2. Podział zadań programistycznych

### MOD-01 – Fundament aplikacji i logowanie

**Odpowiedzialność:** Członek 1  
**Folder:** `modules/auth/` oraz `app.py`

- **DEV-01:** Przygotowanie głównego szkieletu aplikacji Streamlit, podstawowego układu interfejsu i nawigacji.
- **DEV-02:** Implementacja formularzy rejestracji i logowania użytkowników oraz bezpiecznego haszowania haseł.
- **DEV-03:** Implementacja logowania, wylogowania i obsługi sesji użytkownika przy wykorzystaniu funkcji bazy danych.

**Rezultat:** Działający fundament aplikacji z możliwością nawigacji i obsługą kont użytkowników.

### MOD-02 – Kalkulator wartości odżywczych

**Odpowiedzialność:** Członek 2  
**Folder:** `modules/calculator/`

- **DEV-04:** Stworzenie formularza kalkulatora w Streamlit do wprowadzania danych z etykiety na 100 g lub 100 ml.
- **DEV-05:** Implementacja przeliczania kalorii, białka, tłuszczów i węglowodanów na dowolną ilość produktu.
- **DEV-06:** Walidacja danych wejściowych i testowanie poprawności obliczeń.

**Rezultat:** Działający kalkulator wartości odżywczych przygotowany do integracji z dziennikiem żywieniowym.

### MOD-03 – Baza danych SQLite

**Odpowiedzialność:** Członek 3  
**Folder:** `modules/database/`

- **DEV-07:** Utworzenie lokalnej bazy SQLite oraz tabel użytkowników, produktów, wpisów żywieniowych i celów.
- **DEV-08:** Implementacja funkcji zapisywania, odczytywania, edytowania i usuwania danych.
- **DEV-09:** Obsługa danych użytkowników i ich powiązania z wpisami żywieniowymi oraz celami.

**Rezultat:** Działająca baza SQLite udostępniająca funkcje potrzebne pozostałym modułom.

### MOD-04 – Dziennik żywieniowy, cele i historia

**Odpowiedzialność:** Członek 4  
**Folder:** `modules/diary/`

- **DEV-10:** Implementacja dodawania przeliczonych produktów do dziennika dla wybranej daty.
- **DEV-11:** Stworzenie widoku dziennika z możliwością przeglądania, edytowania i usuwania wpisów.
- **DEV-12:** Automatyczne sumowanie kalorii i makroskładników oraz obsługa dziennych celów żywieniowych.
- **DEV-13:** Implementacja historii spożycia z możliwością przeglądania poprzednich dni.

**Rezultat:** Działający dziennik żywieniowy umożliwiający zapisywanie posiłków, kontrolowanie dziennych celów oraz sprawdzanie historii.

## 3. Organizacja Backlogu

Każdy z czterech modułów posiada główne Issue na GitHubie.

Poszczególne Dev Taski będą tworzone jako Sub-issues przypisane do odpowiedniego modułu i osoby odpowiedzialnej.

Do monitorowania pracy wykorzystywane będą statusy:

- **Todo** – zadanie oczekuje na realizację.
- **In Progress** – zadanie jest wykonywane.
- **In Review** – zadanie oczekuje na sprawdzenie.
- **Done** – zadanie zostało ukończone i zaakceptowane.

## 4. Kolejność realizacji

Prace nad modułami mogą odbywać się równolegle.

Na początku zespół uzgadnia podstawową strukturę aplikacji oraz sposób komunikacji między modułami.

MOD-01 przygotowuje fundament aplikacji, MOD-02 tworzy niezależny kalkulator, MOD-03 opracowuje bazę danych, a MOD-04 przygotowuje dziennik żywieniowy.

Do czasu integracji poszczególne moduły mogą korzystać z przykładowych danych testowych.

Po przygotowaniu funkcjonalności moduły zostaną połączone w jedną aplikację.

## 5. Integracja i testowanie

Za końcową integrację i testowanie odpowiada cały zespół w ramach zadania **TEST-01**.

Zakres obejmuje sprawdzenie poprawności działania modułów, testy zapisu i odczytu danych, testy interfejsu na komputerze i urządzeniach mobilnych oraz poprawianie wykrytych błędów.

## 6. Podsumowanie

Projekt CalorieTracker został podzielony na cztery główne moduły i 13 zadań technicznych.

Podział umożliwia równoległą pracę członków zespołu, kontrolowanie postępów za pomocą GitHub Projects i stopniową integrację wszystkich funkcjonalności.

**Planowany termin ukończenia projektu: 22 stycznia 2027 r.**
