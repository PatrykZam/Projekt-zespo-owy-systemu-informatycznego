# CalorieTracker – Opis projektu i wymagania

## 1. Informacje o projekcie

**Nazwa:** CalorieTracker

**Rodzaj:** Lokalna aplikacja webowa do liczenia kalorii i makroskładników, dostosowana do komputerów oraz urządzeń mobilnych.

**Technologie:** Python, Streamlit, SQLite.

**Zespół:** 4 osoby.

**Planowany termin ukończenia:** 22 stycznia 2027 r.

## 2. Cel projektu

Celem projektu jest stworzenie prostej aplikacji umożliwiającej użytkownikowi monitorowanie dziennego spożycia kalorii oraz makroskładników: białka, tłuszczów i węglowodanów.

Główną funkcjonalnością aplikacji będzie kalkulator pozwalający przeliczać wartości odżywcze produktów na podstawie informacji podanych na etykietach. Użytkownik wprowadzi wartości na 100 g lub 100 ml, a następnie dowolną ilość spożytego produktu. Aplikacja automatycznie obliczy odpowiadającą jej wartość energetyczną i zawartość makroskładników.

Dodatkowo aplikacja umożliwi zapisywanie spożytych produktów, ustalanie dziennych celów żywieniowych oraz przeglądanie historii.

Projekt realizowany jest w ramach zajęć akademickich. Jego celem jest stworzenie działającej aplikacji oraz przedstawienie organizacji pracy zespołowej z wykorzystaniem GitHuba.

## 3. Grupa docelowa

Aplikacja przeznaczona jest dla osób, które chcą kontrolować swoją dietę, w szczególności:

- Osób monitorujących dzienne spożycie kalorii.
- Osób aktywnych fizycznie, kontrolujących makroskładniki.
- Osób chcących prowadzić dziennik żywieniowy.
- Osób potrzebujących prostego kalkulatora do przeliczania wartości odżywczych produktów.

Aplikacja ma charakter demonstracyjny i nie jest przeznaczona do komercyjnego udostępniania.

## 4. Opis działania aplikacji

Po uruchomieniu aplikacji użytkownik będzie mógł utworzyć konto lub zalogować się na istniejące.

Po zalogowaniu uzyska dostęp do swojego dziennika żywieniowego, kalkulatora kalorii, historii spożycia i dziennych celów.

### Kalkulator wartości odżywczych

Użytkownik będzie mógł przepisać z etykiety produktu jego nazwę oraz wartości odżywcze na 100 g lub 100 ml:

- Kalorie (kcal).
- Białko (g).
- Tłuszcze (g).
- Węglowodany (g).

Następnie poda ilość, którą faktycznie spożył. Aplikacja automatycznie przeliczy wartości na tę ilość.

**Przykład:**

Użytkownik kupuje pitny skyr o pojemności 500 ml. Na etykiecie znajdują się wartości na 100 ml, przykładowo 70 kcal i 8 g białka.

Po wpisaniu wartości z etykiety oraz ilości 500 ml aplikacja oblicza:

- Kalorie: 350 kcal.
- Białko: 40 g.

Analogicznie przeliczane są tłuszcze i węglowodany.

Kalkulator pozwoli przeliczać produkty na dowolną dodatnią ilość, np. 50 g, 250 g, 500 g czy 1 kg, a w przypadku produktów płynnych na 100 ml, 500 ml czy 1 l.

Jednostka ilości będzie odpowiadać jednostce wartości referencyjnej z etykiety, bez automatycznego utożsamiania gramów z mililitrami.

Po wykonaniu obliczeń użytkownik będzie mógł dodać produkt do dziennika żywieniowego.

### Dziennik i cele żywieniowe

Aplikacja będzie sumowała kalorie i makroskładniki ze wszystkich produktów dodanych do wybranego dnia.

Użytkownik będzie mógł ustalić własne dzienne cele, a aplikacja pokaże ilość spożytych i pozostałych kalorii oraz makroskładników.

Zapisane produkty i podsumowania będzie można przeglądać w historii poprzednich dni.

Dane będą przechowywane w lokalnej bazie SQLite i powiązane z odpowiednim kontem użytkownika.

## 5. Wymagania funkcjonalne

| ID | Wymaganie |
|---|---|
| RF‑01 | System umożliwia rejestrację użytkownika za pomocą nazwy użytkownika i hasła. |
| RF-02 | System umożliwia logowanie i wylogowanie użytkownika. |
| RF-03 | System umożliwia wprowadzenie danych odżywczych produktu na podstawie etykiety, na 100 g lub 100 ml. |
| RF-04 | System umożliwia podanie dowolnej dodatniej ilości produktu, w odpowiedniej jednostce (g, kg, ml lub l). |
| RF-05 | System automatycznie przelicza kalorie, białko, tłuszcze i węglowodany na podaną ilość produktu. |
| RF-06 | System umożliwia dodawanie przeliczonych produktów do dziennika żywieniowego dla wybranej daty. |
| RF-07 | System umożliwia przeglądanie, edytowanie i usuwanie zapisanych wpisów żywieniowych. |
| RF-08 | System automatycznie sumuje kalorie i makroskładniki spożyte w danym dniu. |
| RF-09 | System umożliwia ustawienie i zmianę dziennych celów kalorii, białka, tłuszczów i węglowodanów. |
| RF-10 | System wyświetla postęp realizacji dziennych celów żywieniowych. |
| RF-11 | System umożliwia przeglądanie historii spożytych produktów z poprzednich dni. |
| RF-12 | System zapisuje i odczytuje dane użytkowników, cele oraz dzienniki żywieniowe z bazy SQLite. |
| RF-13 | System przypisuje dane żywieniowe do właściwego konta i wyświetla je odpowiedniemu zalogowanemu użytkownikowi. |

## 6. Wymagania niefunkcjonalne

| ID | Wymaganie |
|---|---|
| RNF‑01 | Aplikacja jest napisana w Pythonie z wykorzystaniem frameworka Streamlit. |
| RNF-02 | Aplikacja działa lokalnie na komputerze. Podstawowe funkcje nie wymagają połączenia z internetem. |
| RNF-03 | Aplikacja posiada responsywny interfejs dostosowany do komputerów i ekranów telefonów. |
| RNF-04 | Planowana jest obsługa urządzeń z systemami Android 16–17 oraz iOS 26–27 za pomocą aktualnych przeglądarek internetowych. |
| RNF-05 | Aplikacja będzie rozwijana i aktualizowana w trakcie realizacji projektu w celu zachowania zgodności z obsługiwanymi środowiskami. |
| RNF-06 | Dostęp z telefonu jest możliwy przez przeglądarkę, gdy urządzenie ma połączenie sieciowe z komputerem uruchamiającym aplikację. |
| RNF-07 | Dane przechowywane są w lokalnej bazie SQLite i pozostają dostępne po ponownym uruchomieniu aplikacji. |
| RNF-08 | Interfejs jest czytelny, intuicyjny i umożliwia wygodną obsługę podstawowych funkcji. |
| RNF-09 | Hasła użytkowników przechowywane są w postaci bezpiecznych hashy, a nie zwykłego tekstu. |
| RNF-10 | System sprawdza poprawność wprowadzanych danych i nie dopuszcza ujemnych wartości odżywczych ani nieprawidłowych ilości produktów. |
| RNF-11 | Obliczenia są wykonywane poprawnie dla obsługiwanych jednostek i prezentowane z ustaloną dokładnością. |
| RNF-12 | Podstawowe operacje, takie jak przeliczanie wartości i wyświetlanie dziennika, powinny działać płynnie na urządzeniach używanych do testowania. |
| RNF-13 | Kod aplikacji jest podzielony na moduły umożliwiające niezależną pracę członków zespołu i ich późniejszą integrację. |

## 7. Zakres projektu

Projekt obejmuje stworzenie działającej aplikacji zawierającej:

- System rejestracji i logowania.
- Kalkulator kalorii i makroskładników na podstawie etykiet.
- Obsługę dowolnych porcji produktów.
- Dziennik żywieniowy.
- Dzienne cele kaloryczne i makroskładników.
- Historię spożycia.
- Lokalną bazę danych SQLite.
- Interfejs dostosowany do komputerów i urządzeń mobilnych.

Aplikacja będzie uruchamiana lokalnie z komputera i obsługiwana przez przeglądarkę internetową. Na telefonach będzie dostępna przez sieć lokalną, bez potrzeby instalowania natywnej aplikacji Android lub iOS.

Projekt nie obejmuje skanowania kodów kreskowych, automatycznego rozpoznawania jedzenia, zewnętrznych baz produktów, płatności ani publicznego hostingu.

## 8. Założenia realizacyjne

- Projekt realizowany jest przez czteroosobowy zespół.
- Kod źródłowy przechowywany jest we wspólnym repozytorium GitHub.
- Zadania organizowane są za pomocą GitHub Issues i GitHub Projects.
- Harmonogram prac prowadzony jest w widoku Roadmap.
- Projekt zostanie podzielony na cztery główne moduły programistyczne.
- Każdy członek zespołu będzie odpowiadał za przydzielone zadania.
- Aplikacja zostanie przetestowana na komputerze oraz wybranych urządzeniach mobilnych.
- Po implementacji moduły zostaną połączone, przetestowane i przygotowane do oddania.

## 9. Oczekiwany rezultat

Rezultatem projektu będzie działająca aplikacja CalorieTracker, umożliwiająca użytkownikom logowanie, automatyczne przeliczanie wartości odżywczych na dowolną porcję, zapisywanie spożytych produktów oraz kontrolowanie dziennych celów żywieniowych.

Aplikacja będzie dostępna na komputerach oraz w przeglądarkach urządzeń mobilnych z systemami Android i iOS.

Dodatkowym rezultatem będzie repozytorium GitHub zawierające kod źródłowy, dokumentację, harmonogram oraz historię pracy zespołu.

**Planowane zakończenie projektu: 22 stycznia 2027 r.**
