import streamlit as st
from modules.auth.auth import show_auth_page
from modules.calculator.calculator_ui import show_calculator

st.set_page_config(
    page_title="CalorieTracker",
    page_icon="🥗",
    layout="centered"
)

# Stan logowania i aktualnego widoku
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None
if "show_login" not in st.session_state:
    st.session_state["show_login"] = False


def wyloguj():
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["user_id"] = None
    st.session_state["show_login"] = False
    st.rerun()


def main():
    zalogowany = st.session_state["logged_in"]

    # Gość może przejść do logowania i wrócić do kalkulatora.
    if not zalogowany and st.session_state["show_login"]:
        if st.button("← Wróć do kalkulatora"):
            st.session_state["show_login"] = False
            st.rerun()

        show_auth_page()
        return

    # Górny pasek jest widoczny dla gości i zalogowanych.
    lewa, prawa = st.columns([3, 1], vertical_alignment="center")

    with lewa:
        st.markdown("### 🥗 CalorieTracker")

    with prawa:
        if zalogowany:
            if st.button("Wyloguj się", use_container_width=True):
                wyloguj()
        else:
            if st.button(
                "Zaloguj się",
                type="primary",
                use_container_width=True
            ):
                st.session_state["show_login"] = True
                st.rerun()

    # Kalkulator działa bez logowania.
    if not zalogowany:
        st.caption(
            "Tryb gościa — kalkulator jest dostępny bez konta. "
            "Zaloguj się, aby korzystać z dziennika, celów i historii."
        )
        show_calculator()
        return

    # Pozostałe funkcje są dostępne po zalogowaniu.
    with st.sidebar:
        st.write(f"👤 Zalogowano jako: **{st.session_state['username']}**")
        menu = st.radio(
            "Nawigacja",
            ["🧮 Kalkulator porcji", "📔 Dziennik żywieniowy", "🎯 Cele i historia"]
        )

    if menu == "🧮 Kalkulator porcji":
        show_calculator()

    elif menu == "📔 Dziennik żywieniowy":
        st.header("📔 Twój dziennik żywieniowy")
        st.info("Miejsce na moduł MOD-04 (Dziennik posiłków - Osoba 4)")

    elif menu == "🎯 Cele i historia":
        st.header("🎯 Dzienne cele i historia")
        st.info("Miejsce na moduł MOD-04 (Cele i historia - Osoba 4)")


if __name__ == "__main__":
    main()
