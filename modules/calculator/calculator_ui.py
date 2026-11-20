
import streamlit as st
from modules.calculator.calculator_logic import przelicz_wartosci


def formatuj(liczba):
    return f"{liczba:.2f}".replace(".", ",").rstrip("0").rstrip(",")


def wyczysc_wynik():
    st.session_state.pop("mod02_wynik", None)


def show_calculator():
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

    st.divider()

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
                placeholder="Np. Skyr naturalny"
            )

            st.caption(f"Wartości odżywcze na {podstawa}")

            col1, col2 = st.columns(2)

            with col1:
                kcal = st.number_input(
                    "Kalorie (kcal)",
                    min_value=0.0,
                    step=1.0,
                    format="%.2f"
                )
                bialko = st.number_input(
                    "Białko (g)",
                    min_value=0.0,
                    step=0.1,
                    format="%.2f"
                )

            with col2:
                tluszcze = st.number_input(
                    "Tłuszcze (g)",
                    min_value=0.0,
                    step=0.1,
                    format="%.2f"
                )
                weglowodany = st.number_input(
                    "Węglowodany (g)",
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

            except ValueError as blad:
                st.error(str(blad))
                wyczysc_wynik()

    wynik = st.session_state.get("mod02_wynik")

    if wynik:
        with st.container(key="mod02_wyniki"):
            st.divider()
            st.subheader("📊 Wyniki obliczeń")

            st.write(f"**Produkt:** {wynik['nazwa']}")
            st.caption(
                f"Porcja: {formatuj(wynik['ilosc'])} "
                f"{wynik['jednostka']}"
            )

            st.metric(
                "🔥 Łączna energia",
                f"{formatuj(wynik['kcal'])} kcal"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🥩 Białko",
                    f"{formatuj(wynik['bialko'])} g"
                )

            with col2:
                st.metric(
                    "🥑 Tłuszcze",
                    f"{formatuj(wynik['tluszcze'])} g"
                )

            with col3:
                st.metric(
                    "🌾 Węglowodany",
                    f"{formatuj(wynik['weglowodany'])} g"
                )

            st.success("Obliczenia wykonane poprawnie.")

            if st.button("Wyczyść wynik", key="mod02_clear"):
                wyczysc_wynik()
                st.rerun()


if __name__ == "__main__":
    show_calculator()
