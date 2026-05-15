import streamlit as st
import pandas as pd
from scripts.db_config import get_connection
from scripts.db_queries import queries, insights

st.set_page_config(
    page_title="Traffic Crash Analysis Dashboard",
    layout="wide"
)

st.title("Traffic Crash Analysis Report")
st.write("Interactive analysis of traffic crash data using SQL queries executed on a MySQL database.")

selected_query = st.selectbox(
    "Select Analysis",
    list(queries.keys())
)

try:
    conn = get_connection()
    cursor = conn.cursor()

    df = pd.read_sql(queries[selected_query], conn)

    st.subheader(selected_query)
    st.dataframe(df, use_container_width=True)

    st.info(insights[selected_query])

except Exception as e:
    st.error(f"Error: {e}")

finally:
    if "cursor" in locals():
        cursor.close()

    if "conn" in locals():
        conn.close()