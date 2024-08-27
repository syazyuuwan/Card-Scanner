import streamlit as st 
import pandas as pd

data_df = pd.read_csv("leads.csv")

if st.button("Refresh"):
    data_df = pd.read_csv("leads.csv")

if data_df is not None:
    st.data_editor(data_df, hide_index=True, use_container_width=True,num_rows="dynamic")