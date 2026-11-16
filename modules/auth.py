import streamlit as st

def show_auth_page():
    """Wyświetla formularze logowania i rejestracji dla niezalogowanego użytkownika."""
    st.title("🥗 CalorieTracker")
    st.subheader("Zaloguj się lub utwórz konto, aby zarządzać swoją dietą")

    tab_login, tab_register = st.tabs(["Logowanie", "Rejestracja"])

    # --- ZAKŁADKA LOGOWANIA ---
    with tab_login:
        with st.form("login_form"):
            username = st.text_input("Nazwa użytkownika")
            password = st.text_input("Hasło", type="password")
            submitted = st.form_submit_button("Zaloguj się")

            if submitted:
                if not username or not password:
                    st.error("Wypełnij wszystkie pola!")
                else:
                    # TODO: Podpiąć weryfikację hasła z bazy SQLite (MOD-03)
                    # Tymczasowe logowanie testowe:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["user_id"] = 1
                    st.success(f"Zalogowano jako {username}!")
                    st.rerun()

    # --- ZAKŁADKA REJESTRACJI ---
    with tab_register:
        with st.form("register_form"):
            new_user = st.text_input("Wybierz nazwę użytkownika")
            new_pass = st.text_input("Hasło", type="password")
            confirm_pass = st.text_input("Powtórz hasło", type="password")
            reg_submitted = st.form_submit_button("Utwórz konto")

            if reg_submitted:
                if not new_user or not new_pass:
                    st.error("Wszystkie pola są wymagane.")
                elif new_pass != confirm_pass:
                    st.error("Hasła nie są identyczne!")
                else:
                    # TODO: Podpiąć zapis nowego użytkownika do SQLite (MOD-03)
                    st.success("Konto utworzone (tryb testowy)! Możesz się teraz zalogować.")
