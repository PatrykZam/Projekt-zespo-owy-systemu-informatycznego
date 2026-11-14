# ORG-02 – User Stories

**Projekt:** CalorieTracker  
**Typ dokumentu:** Historie użytkownika, kryteria akceptacji i macierz powiązań  
**Planowany termin zakończenia projektu:** 22 stycznia 2027 r.

## 1. Historie użytkownika (User Stories)

Historie użytkownika opisują najważniejsze funkcjonalności aplikacji CalorieTracker z perspektywy użytkownika. Każda historia określa potrzebę użytkownika oraz cel, który chce osiągnąć za pomocą aplikacji.

### US-01 – Rejestracja konta

**Jako** nowy użytkownik, **chcę** utworzyć konto za pomocą nazwy użytkownika i hasła, **aby** móc korzystać z własnego dziennika żywieniowego i zapisywać swoje dane.

### US-02 – Logowanie i wylogowanie

**Jako** zarejestrowany użytkownik, **chcę** zalogować się i wylogować z aplikacji, **aby** uzyskiwać dostęp do swoich danych i chronić je przed dostępem innych osób.

### US-03 – Przeliczanie wartości odżywczych

**Jako** użytkownik, **chcę** wprowadzić wartości odżywcze produktu z etykiety oraz ilość spożytego produktu, **aby** obliczyć kalorie, białko, tłuszcze i węglowodany dla wybranej porcji.

### US-04 – Dodawanie produktu do dziennika

**Jako** użytkownik, **chcę** dodawać obliczone produkty do dziennika dla wybranej daty, **aby** zapisywać swoje posiłki i monitorować spożycie.

### US-05 – Edytowanie i usuwanie wpisów

**Jako** użytkownik, **chcę** edytować i usuwać wpisy w dzienniku żywieniowym, **aby** poprawiać błędy i utrzymywać poprawne dane o spożytych produktach.

### US-06 – Podsumowanie dziennego spożycia

**Jako** użytkownik, **chcę** zobaczyć sumę kalorii, białka, tłuszczów i węglowodanów spożytych w ciągu dnia, **aby** kontrolować swoje odżywianie.

### US-07 – Ustalanie dziennych celów

**Jako** użytkownik, **chcę** ustawiać i zmieniać dzienne cele dotyczące kalorii i makroskładników, **aby** dostosować je do swoich indywidualnych potrzeb.

### US-08 – Monitorowanie postępów

**Jako** użytkownik, **chcę** sprawdzać postęp realizacji dziennych celów żywieniowych, **aby** wiedzieć, ile kalorii i makroskładników już spożyłem oraz ile pozostało mi do osiągnięcia celu.

### US-09 – Przeglądanie historii spożycia

**Jako** użytkownik, **chcę** przeglądać dzienniki żywieniowe z poprzednich dni, **aby** analizować swoje wcześniejsze spożycie kalorii i makroskładników.

---

## 2. Kryteria akceptacji (Acceptance Criteria)

Kryteria akceptacji określają warunki, które muszą zostać spełnione, aby daną historię użytkownika można było uznać za zrealizowaną.

### US-01 – Rejestracja konta

- **AC-01.1:** System umożliwia wprowadzenie nazwy użytkownika i hasła.
- **AC-01.2:** System odrzuca rejestrację, jeśli wymagane pola są puste.
- **AC-01.3:** System nie pozwala na utworzenie drugiego konta z już zajętą nazwą użytkownika.
- **AC-01.4:** Hasło jest przechowywane w postaci bezpiecznego hasha, a nie zwykłego tekstu.
- **AC-01.5:** Po poprawnej rejestracji konto zostaje zapisane w bazie SQLite.

### US-02 – Logowanie i wylogowanie

- **AC-02.1:** Użytkownik może zalogować się przy użyciu poprawnej nazwy użytkownika i hasła.
- **AC-02.2:** System odrzuca próbę logowania przy nieprawidłowych danych.
- **AC-02.3:** Po zalogowaniu użytkownik uzyskuje dostęp do funkcji aplikacji i własnych danych.
- **AC-02.4:** Użytkownik może wylogować się z aplikacji.
- **AC-02.5:** Po wylogowaniu dostęp do funkcji wymagających zalogowania jest zablokowany.

### US-03 – Przeliczanie wartości odżywczych

- **AC-03.1:** Użytkownik może wprowadzić nazwę produktu oraz wartości kalorii, białka, tłuszczów i węglowodanów na 100 g lub 100 ml.
- **AC-03.2:** Użytkownik może wybrać odpowiednią jednostkę i podać ilość produktu w gramach, kilogramach, mililitrach lub litrach.
- **AC-03.3:** System przelicza wartości odżywcze proporcjonalnie do podanej ilości.
- **AC-03.4:** System nie dopuszcza ujemnych wartości odżywczych ani ilości równej zero.
- **AC-03.5:** System sprawdza poprawność danych i wyświetla komunikat w przypadku błędnych wartości.
- **AC-03.6:** Wyniki są prezentowane z ustaloną dokładnością.
- **AC-03.7:** System nie utożsamia automatycznie gramów z mililitrami.

**Przykład testowy:** Produkt zawiera 70 kcal i 8 g białka na 100 ml. Po wpisaniu ilości 500 ml system wyświetla 350 kcal i 40 g białka.

### US-04 – Dodawanie produktu do dziennika

- **AC-04.1:** Użytkownik może dodać poprawnie przeliczony produkt do dziennika.
- **AC-04.2:** Użytkownik może wybrać datę, do której zostanie przypisany wpis.
- **AC-04.3:** Wpis zawiera nazwę produktu, ilość, jednostkę oraz obliczone wartości odżywcze.
- **AC-04.4:** Zapisany wpis jest dostępny po ponownym uruchomieniu aplikacji.
- **AC-04.5:** Wpis zostaje przypisany do zalogowanego użytkownika.

### US-05 – Edytowanie i usuwanie wpisów

- **AC-05.1:** Użytkownik może wybrać zapisany wpis ze swojego dziennika.
- **AC-05.2:** Użytkownik może zmienić dane wpisu, w tym ilość produktu.
- **AC-05.3:** Po zapisaniu zmian system aktualizuje wartości odżywcze wpisu.
- **AC-05.4:** Użytkownik może usunąć wybrany wpis.
- **AC-05.5:** Po edycji lub usunięciu system aktualizuje dzienne podsumowanie.
- **AC-05.6:** Użytkownik nie może edytować ani usuwać wpisów należących do innego konta.

### US-06 – Podsumowanie dziennego spożycia

- **AC-06.1:** System sumuje kalorie, białko, tłuszcze i węglowodany ze wszystkich wpisów wybranego dnia.
- **AC-06.2:** Podsumowanie dotyczy wyłącznie wpisów zalogowanego użytkownika.
- **AC-06.3:** Dodanie, edycja lub usunięcie wpisu powoduje aktualizację podsumowania.
- **AC-06.4:** Gdy w danym dniu nie ma wpisów, system wyświetla zerowe spożycie.
- **AC-06.5:** Użytkownik może wyświetlić podsumowanie dla wybranej daty.

### US-07 – Ustalanie dziennych celów

- **AC-07.1:** Użytkownik może ustawić dzienny cel kalorii, białka, tłuszczów i węglowodanów.
- **AC-07.2:** System odrzuca ujemne wartości celów.
- **AC-07.3:** Użytkownik może zmienić wcześniej zapisane cele.
- **AC-07.4:** Cele są zapisywane w bazie SQLite i dostępne po ponownym uruchomieniu aplikacji.
- **AC-07.5:** Cele są przypisane do właściwego konta użytkownika.

### US-08 – Monitorowanie postępów

- **AC-08.1:** System wyświetla aktualne spożycie kalorii i makroskładników w odniesieniu do dziennych celów.
- **AC-08.2:** System oblicza pozostałą ilość kalorii i każdego makroskładnika do osiągnięcia celu.
- **AC-08.3:** Jeżeli użytkownik przekroczy cel, system wyświetla przekroczenie zamiast ujemnej wartości jako pozostałej ilości.
- **AC-08.4:** Postęp jest aktualizowany po zmianie wpisów w dzienniku.
- **AC-08.5:** Jeśli cel nie został ustawiony, system informuje o braku celu zamiast wykonywać nieprawidłowe obliczenia.

### US-09 – Przeglądanie historii spożycia

- **AC-09.1:** Użytkownik może wybrać wcześniejszą datę i wyświetlić zapisane wpisy.
- **AC-09.2:** System wyświetla produkty zapisane dla wybranego dnia.
- **AC-09.3:** System prezentuje podsumowanie kalorii i makroskładników dla wybranego dnia.
- **AC-09.4:** Historia pozostaje dostępna po ponownym uruchomieniu aplikacji.
- **AC-09.5:** Użytkownik ma dostęp wyłącznie do historii przypisanej do własnego konta.

---

## 3. Powiązanie historii z funkcjami aplikacji

Poniższa tabela przedstawia powiązanie historii użytkownika z wymaganiami funkcjonalnymi zdefiniowanymi w opisie projektu.

| ID historii | Funkcja aplikacji | Powiązane wymagania |
|---|---|---|
| US-01 | Rejestracja użytkownika | RF-01, RF-12, RF-13 |
| US-02 | Logowanie i wylogowanie | RF-02, RF-13 |
| US-03 | Kalkulator wartości odżywczych | RF-03, RF-04, RF-05 |
| US-04 | Dodawanie produktów do dziennika | RF-06, RF-12, RF-13 |
| US-05 | Edycja i usuwanie wpisów | RF-07, RF-12, RF-13 |
| US-06 | Dzienne podsumowanie spożycia | RF-08 |
| US-07 | Ustawianie i zmiana celów | RF-09, RF-12, RF-13 |
| US-08 | Prezentacja postępów w realizacji celów | RF-10 |
| US-09 | Historia spożycia | RF-11, RF-12, RF-13 |

### Uzupełniające powiązania z wymaganiami niefunkcjonalnymi

- **RNF-01:** Wszystkie historie są realizowane w aplikacji napisanej w Pythonie z wykorzystaniem Streamlit.
- **RNF-02, RNF-06, RNF-07:** Aplikacja działa lokalnie, korzysta z bazy SQLite i umożliwia dostęp z urządzeń mobilnych przez sieć lokalną.
- **RNF-03, RNF-04, RNF-08:** Interfejs powinien być czytelny i dostosowany do komputerów oraz obsługiwanych przeglądarek mobilnych.
- **RNF-05:** Aplikacja jest rozwijana i aktualizowana w trakcie realizacji projektu.
- **RNF-09:** Hasła są przechowywane w postaci bezpiecznych hashy.
- **RNF-10, RNF-11:** Dane wejściowe są walidowane, a obliczenia wykonywane poprawnie dla obsługiwanych jednostek.
- **RNF-12:** Podstawowe operacje powinny działać płynnie na urządzeniach testowych.
- **RNF-13:** Kod jest podzielony na moduły umożliwiające równoległą pracę członków zespołu.

---

## 4. Podsumowanie

Przygotowane historie użytkownika obejmują podstawowe funkcjonalności aplikacji CalorieTracker: zarządzanie kontem, przeliczanie wartości odżywczych, prowadzenie dziennika, kontrolowanie dziennych celów oraz przeglądanie historii spożycia.

Każda historia posiada kryteria akceptacji, które pozwalają zweryfikować poprawność implementacji podczas testowania aplikacji.

Macierz powiązań umożliwia sprawdzenie, czy wymagania funkcjonalne określone w dokumentacji projektu zostały uwzględnione w planowanych funkcjach aplikacji.

Dokument może służyć jako podstawa do tworzenia zadań w GitHub Issues, planowania prac w GitHub Projects oraz przygotowania testów akceptacyjnych.
