import streamlit as st
from modules.auth import show_auth_page

# Konfiguracja podstawowa strony (musi być jako pierwsza komenda Streamlit)
st.set_page_config(
    page_title="CalorieTracker",
    page_icon="🥗",
    layout="centered"
)

# Inicjalizacja zmiennych sesji
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None


def main():
    # Jeśli użytkownik nie jest zalogowany -> pokaż ekran logowania
    if not st.session_state["logged_in"]:
        show_auth_page()
        return

    # --- PANEL ZALOGOWANEGO UŻYTKOWNIKA ---
    with st.sidebar:
        st.write(f"👤 Zalogowano jako: **{st.session_state['username']}**")
        menu = st.radio(
            "Nawigacja",
            ["🧮 Kalkulator porcji", "📔 Dziennik żywieniowy", "🎯 Cele i historia"]
        )
        st.divider()
        if st.button("Wyloguj się"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = None
            st.session_state["user_id"] = None
            st.rerun()

    # Routing (przełączanie ekranów - miejsca na moduły kolegów)
    if menu == "🧮 Kalkulator porcji":
        st.header("🧮 Kalkulator wartości odżywczych")
        st.info("Miejsce na moduł MOD-02 (Kalkulator porcji - Osoba 2)")

    elif menu == "📔 Dziennik żywieniowy":
        st.header("📔 Twój dziennik żywieniowy")
        st.info("Miejsce na moduł MOD-04 (Dziennik posiłków - Osoba 4)")

    elif menu == "🎯 Cele i historia":
        st.header("🎯 Dzienne cele i historia")
        st.info("Miejsce na moduł MOD-04 (Cele i historia - Osoba 4)")


if __name__ == "__main__":
    main()
