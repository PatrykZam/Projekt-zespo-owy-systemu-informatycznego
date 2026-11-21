
import streamlit as st
from modules.calculator.calculator_logic import przelicz_wartosci


def formatuj(liczba):
    return f"{liczba:.2f}".replace(".", ",").rstrip("0").rstrip(",")


def wyczysc_wynik():
    st.session_state.pop("mod02_wynik", None)


def show_calculator():
    if "mod02_widok" not in st.session_state:
        st.session_state["mod02_widok"] = "formularz"

    # Streamlit usuwa stan pól, które nie są wyświetlane.
    # Po wejściu w edycję przywracamy dane z niezależnej kopii.
    if st.session_state.pop("mod02_przywroc_edycje", False):
        for klucz, wartosc in st.session_state.get("mod02_draft", {}).items():
            st.session_state[klucz] = wartosc

    st.markdown("""
        <style>
        .st-key-mod02_formularz [data-testid="stForm"] {
            border: 1px solid rgba(110, 180, 140, 0.25);
            border-radius: 18px;
            padding: 24px;
        }

        .st-key-mod02_wyniki [data-testid="stMetric"] {
            background: rgba(70, 150, 110, 0.10);
            border: 1px solid rgba(110, 180, 140, 0.20);
            border-radius: 15px;
            padding: 18px;
        }

        .st-key-mod02_wyniki [data-testid="stMetricValue"] {
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

    st.caption("CALORIETRACKER  /  MOD-02")
    st.title("🥗 Kalkulator wartości odżywczych")
    st.write(
        "Przepisz wartości z etykiety i sprawdź, "
        "ile kalorii oraz makroskładników zawiera Twoja porcja."
    )

    # Na telefonie i komputerze wynik ma własny widok,
    # zamiast pojawiać się pod długim formularzem.
    if (
        st.session_state["mod02_widok"] == "wynik"
        and "mod02_wynik" in st.session_state
    ):
        wynik = st.session_state["mod02_wynik"]

        with st.container(key="mod02_wyniki"):
            st.subheader(wynik["nazwa"])
            st.caption(
                f"Wartości dla porcji: {formatuj(wynik['ilosc'])} "
                f"{wynik['jednostka']}"
            )

            st.metric(
                "🔥 Łączna energia",
                f"{formatuj(wynik['kcal'])} kcal"
            )

            kol1, kol2, kol3 = st.columns(3)
            with kol1:
                st.metric("🥩 Białko", f"{formatuj(wynik['bialko'])} g")
            with kol2:
                st.metric("🥑 Tłuszcze", f"{formatuj(wynik['tluszcze'])} g")
            with kol3:
                st.metric(
                    "🌾 Węglowodany",
                    f"{formatuj(wynik['weglowodany'])} g"
                )

            st.divider()
            edycja, nowy = st.columns(2)

            with edycja:
                if st.button(
                    "✏️ Edytuj produkt",
                    use_container_width=True,
                    key="mod02_edytuj"
                ):
                    st.session_state["mod02_widok"] = "formularz"
                    st.session_state["mod02_przywroc_edycje"] = True
                    st.rerun()

            with nowy:
                if st.button(
                    "➕ Nowy produkt",
                    use_container_width=True,
                    type="primary",
                    key="mod02_nowy"
                ):
                    wyczysc_wynik()
                    st.session_state.pop("mod02_draft", None)
                    st.session_state.pop("mod02_przywroc_edycje", None)
                    for klucz in [
                        "mod02_podstawa", "mod02_jednostka",
                        "mod02_nazwa", "mod02_kcal", "mod02_bialko",
                        "mod02_tluszcze", "mod02_weglowodany",
                        "mod02_ilosc_g", "mod02_ilosc_kg",
                        "mod02_ilosc_ml", "mod02_ilosc_l"
                    ]:
                        st.session_state.pop(klucz, None)
                    st.session_state["mod02_widok"] = "formularz"
                    st.rerun()

        return

    with st.container(key="mod02_formularz"):
        st.subheader("📦 Dane produktu")

        podstawa = st.radio(
            "Wartości na etykiecie podane dla:",
            ["100 g", "100 ml"],
            horizontal=True,
            key="mod02_podstawa",
            on_change=wyczysc_wynik
        )

        st.subheader("⚖️ Wielkość porcji")

        if podstawa == "100 g":
            jednostki = ["g", "kg"]
        else:
            jednostki = ["ml", "l"]

        jednostka = st.selectbox(
            "Jednostka spożytej ilości",
            jednostki,
            key="mod02_jednostka",
            on_change=wyczysc_wynik
        )

        with st.form("mod02_form"):
            nazwa = st.text_input(
                "Nazwa produktu",
                placeholder="Np. Skyr naturalny",
                key="mod02_nazwa"
            )

            st.caption(f"Wartości odżywcze na {podstawa}")

            col1, col2 = st.columns(2)

            with col1:
                kcal = st.number_input(
                    "Kalorie (kcal)",
                    key="mod02_kcal",
                    min_value=0.0,
                    step=1.0,
                    format="%.2f"
                )
                bialko = st.number_input(
                    "Białko (g)",
                    key="mod02_bialko",
                    min_value=0.0,
                    step=0.1,
                    format="%.2f"
                )

            with col2:
                tluszcze = st.number_input(
                    "Tłuszcze (g)",
                    key="mod02_tluszcze",
                    min_value=0.0,
                    step=0.1,
                    format="%.2f"
                )
                weglowodany = st.number_input(
                    "Węglowodany (g)",
                    key="mod02_weglowodany",
                    min_value=0.0,
                    step=0.1,
                    format="%.2f"
                )

            domyslna_ilosc = (
                100.0 if jednostka in ["g", "ml"] else 0.1
            )

            ilosc = st.number_input(
                f"Spożyta ilość ({jednostka})",
                min_value=0.01,
                value=domyslna_ilosc,
                step=0.1,
                format="%.2f",
                key=f"mod02_ilosc_{jednostka}"
            )

            oblicz = st.form_submit_button(
                "🧮 Oblicz wartości odżywcze",
                type="primary",
                use_container_width=True
            )

    if oblicz:
        if not nazwa.strip():
            st.error("Wprowadź nazwę produktu.")
            wyczysc_wynik()
        else:
            try:
                wyniki = przelicz_wartosci(
                    kcal,
                    bialko,
                    tluszcze,
                    weglowodany,
                    ilosc,
                    jednostka
                )

                st.session_state["mod02_wynik"] = {
                    "nazwa": nazwa.strip(),
                    "ilosc": ilosc,
                    "jednostka": jednostka,
                    "podstawa": podstawa,
                    **wyniki
                }
                # Kopia oryginalnych danych pozwala później edytować produkt.
                # To osobny stan, niepowiązany z polami formularza.
                st.session_state["mod02_draft"] = {
                    "mod02_podstawa": podstawa,
                    "mod02_jednostka": jednostka,
                    "mod02_nazwa": nazwa,
                    "mod02_kcal": kcal,
                    "mod02_bialko": bialko,
                    "mod02_tluszcze": tluszcze,
                    "mod02_weglowodany": weglowodany,
                    f"mod02_ilosc_{jednostka}": ilosc
                }
                st.session_state["mod02_widok"] = "wynik"
                st.rerun()

            except ValueError as blad:
                st.error(str(blad))
                wyczysc_wynik()



if __name__ == "__main__":
    show_calculator()
