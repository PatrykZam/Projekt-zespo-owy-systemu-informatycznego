ORG-03 – Zadania programistyczne (Dev Tasks) i Backlog
Projekt: CalorieTracker
Typ dokumentu: Podział funkcjonalny na zadania techniczne, organizacja backlogu i priorytetyzacja
Planowany termin ukończenia projektu: 22 stycznia 2027 r.

1. Wprowadzenie do zadań technicznych (Dev Tasks)
Zadania techniczne stanowią rozwinięcie wymagań funkcjonalnych oraz historii użytkownika (User Stories) na konkretne kroki programistyczne realizowane w zespole. Każde zadanie techniczne odpowiada elementowi kodu tworzonego w Pythonie przy użyciu frameworka Streamlit i lokalnej bazy danych SQLite.

2. Podział zadań na moduły programistyczne
W ramach czteroosobowego zespołu prace zostały podzielone na cztery główne moduły techniczne, powiązane z odpowiednimi osobami:

Moduł 1: Baza danych i Użytkownicy (Odpowiedzialność: Członek 1 i Członek 2)
- DEV-01: Konfiguracja lokalnej bazy danych SQLite i schematu tabel (tabeli użytkowników, produktów, wpisów oraz celów).
- DEV-02: Implementacja rejestracji użytkownika oraz bezpiecznego haszowania haseł.
- DEV-03: Implementacja logowania, wylogowania oraz obsługi sesji użytkownika w Streamlit.

Moduł 2: Kalkulator wartości odżywczych (Odpowiedzialność: Członek 3)
- DEV-04: Stworzenie formularza wprowadzania danych z etykiety (wartości na 100 g / 100 ml).
- DEV-05: Implementacja logiki matematycznej przeliczania wartości odżywczych na podaną ilość produktu (obsługa gramów, kilogramów, mililitrów i litrów).
- DEV-06: Walidacja danych wejściowych kalkulatora (blokowanie ujemnych wartości, zerowych ilości i błędów).

Moduł 3: Dziennik żywieniowy i Cele (Odpowiedzialność: Członek 4)
- DEV-07: Implementacja dodawania przeliczonego produktu do dziennika dla wybranej daty.
- DEV-08: Stworzenie widoku dziennika z możliwością edycji i usuwania wpisów.
- DEV-09: Automatyczne sumowanie dziennego spożycia kalorii i makroskładników.
- DEV-10: Ustawianie dziennych celów żywieniowych oraz prezentacja postępów (paski postępu i porównanie z celem).

Moduł 4: Historia i Responsywność (Odpowiedzialność: Cały zespół)
- DEV-11: Implementacja przeglądania historii spożycia z poprzednich dni.
- DEV-12: Testy responsywności interfejsu na komputerach i urządzeniach mobilnych w sieci lokalnej.

Moduł 4: Historia i Responsywność (Odpowiedzialność: Cały zespół)
- DEV-11: Implementacja przeglądania historii spożycia z poprzednich dni.
- DEV-12: Testy responsywności interfejsu na komputerach i urządzeniach mobilnych w sieci lokalnej.

3. Organizacja Backlogu i zarządzanie zadaniami
Zadania techniczne są rejestrowane jako GitHub Issues w repozytorium projektu oraz zarządzane w widoku Kanban (GitHub Projects) z użyciem następujących statusów:
- Todo: Zadania zaplanowane do realizacji w kolejnych etapach.
- In Progress: Zadania aktualnie wykonywane przez przypisanego członka zespołu.
- In Review: Zadania po zakończonym kodowaniu, oczekujące na sprawdzenie i połączenie z główną gałęzią.
- Done: Zadania w pełni ukończone, przetestowane i spełniające kryteria akceptacji.

4. Podsumowanie
Podział projektu na konkretne zadania techniczne (Dev Tasks) umożliwia równoległą pracę członków zespołu, śledzenie postępów na GitHubie oraz sprawną integrację poszczególnych modułów aplikacji CalorieTracker do 22 stycznia 2027 r.
