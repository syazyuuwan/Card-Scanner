import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    login_id = st.text_input("ASEM Employee ID:")
    if st.button("Login"):
        if login_id > 0:
            st.session_state.logged_in = True
            st.rerun
        else:
            st.warning("Invalid Login")
            st.rerun
            
def logout():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun
    
login_page = st.Page(login, title = "Login")
logout_page = st.Page(logout, title = "Logout")
leads_page = st.Page("leads.py", title = "Leads Database")
scanner_page = st.Page("scanner.py", title = "Card Scanner")

if st.session_state.logged_in == True:
    pg = st.navigation([leads_page, scanner_page, logout_page])
else:
    pg = st.navigation([login_page])