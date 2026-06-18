import streamlit as st
import pandas as pd
import sqlite3

st.title("Trace")

conn = sqlite3.connect("trace.db")

df = pd.read_sql_query(
    "SELECT * FROM activity",
    conn
)

conn.close()

st.metric(
    "Total Records",
    len(df)
)

st.dataframe(df.tail(20))