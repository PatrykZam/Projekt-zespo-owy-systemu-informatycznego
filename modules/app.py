import streamlit as st
from modules.auth.auth import show_auth_page
from modules.calculator.calculator_ui import show_calculator

st.set_page_config(
    page_title="CalorieTracker",
    page_icon="🥗",
    layout="centered"
)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None
if "user_id" not in st.session_state:
    st.session_state["user_id"] = None


def main():
    if not st.session_state["logged_in"]:
        show_auth_page()
        return

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
