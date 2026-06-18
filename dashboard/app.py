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
    "Total Events",
    len(df)
)

st.subheader("Recent Activity")
st.dataframe(df.tail(20))

st.subheader("Most Used Applications")

if not df.empty:
    app_counts = (
        df["active_app"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(app_counts)