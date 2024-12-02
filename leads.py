import streamlit as st
import pandas as pd
import pygsheets
from google.oauth2 import service_account

SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
my_credentials = service_account.Credentials.from_service_account_info(st.secrets['google_sheets'], scopes=SCOPES)
client = pygsheets.authorize(custom_credentials=my_credentials)

if "editor" not in st.session_state:
    st.session_state.editor = False

@st.cache_data
def get_data():
    #Retrieve workbook ID
    key = client.spreadsheet_ids()[0]
    #Open workbook
    gsheet = client.open_by_key(key)
    #Open corresponding worksheet
    tab = gsheet.worksheet('title','Test')
    df = tab.get_as_df()

    return df

def refresh_data():
    get_data.clear()
    st.rerun()

df = get_data()

if st.session_state.editor == False:
    st.dataframe(df)
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Refresh"):
            refresh_data()
    with col2:
        if st.button("Edit"):
            st.session_state.editor = True
            st.rerun()
else:
    st.data_editor(df)
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Confirm"):
            
            refresh_data()
    with col2:
        if st.button("Cancel"):
            st.session_state.editor = False
            st.rerun()