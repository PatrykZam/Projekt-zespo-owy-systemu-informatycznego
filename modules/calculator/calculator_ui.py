
import streamlit as st
from calculator_logic import przelicz_wartosci


def show_calculator():
    st.title("Kalkulator wartości odżywczych")
    st.write("Wprowadź dane produktu z etykiety.")

    with st.form("calculator_form"):
        nazwa = st.text_input("Nazwa produktu")

        jednostka_etykiety = st.selectbox(
            "Wartości na etykiecie podane dla:",
            ["100 g", "100 ml"]
        )

        kcal = st.number_input("Kalorie (kcal)", min_value=0.0)
        bialko = st.number_input("Białko (g)", min_value=0.0)
        tluszcze = st.number_input("Tłuszcze (g)", min_value=0.0)
        weglowodany = st.number_input("Węglowodany (g)", min_value=0.0)

        st.subheader("Spożyta ilość produktu")

        if jednostka_etykiety == "100 g":
            dostepne_jednostki = ["g", "kg"]
        else:
            dostepne_jednostki = ["ml", "l"]

        jednostka = st.selectbox(
            "Jednostka ilości",
            dostepne_jednostki
        )

        domyslna_ilosc = 100.0 if jednostka in ["g", "ml"] else 0.1

        ilosc = st.number_input(
            f"Spożyta ilość ({jednostka})",
            min_value=0.01,
            value=domyslna_ilosc,
            key=f"ilosc_{jednostka}"
        )

        oblicz = st.form_submit_button("Przelicz")

    if oblicz:
        if not nazwa.strip():
            st.warning("Podaj nazwę produktu.")
        else:
            wyniki = przelicz_wartosci(
                kcal,
                bialko,
                tluszcze,
                weglowodany,
                ilosc,
                jednostka
            )

            st.subheader("Wyniki obliczeń")

            st.write(f"**Produkt:** {nazwa}")
            st.write(f"**Spożyta ilość:** {ilosc:g} {jednostka}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Kalorie", f"{wyniki['kcal']:g} kcal")
                st.metric("Białko", f"{wyniki['bialko']:g} g")

            with col2:
                st.metric("Tłuszcze", f"{wyniki['tluszcze']:g} g")
                st.metric("Węglowodany", f"{wyniki['weglowodany']:g} g")


if __name__ == "__main__":
    show_calculator()
