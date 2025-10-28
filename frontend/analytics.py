import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def add_analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        info = {
            "expense_date1": start_date.strftime("%Y-%m-%d"),
            "expense_date2": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics", json = info)
        response = response.json()
        #st.write(response)

        df = pd.DataFrame(response)
        df_sorted = df.sort_values(by = "Percentage", ascending = False)
        st.title("Expense Breakdown By Category")


        st.bar_chart(
            data=df_sorted.set_index("Category")["Percentage"],
            use_container_width=True
        )
        st.table(df_sorted.style.format({"Total": "{:,.2f}", "Percentage": "{:.2f}"}))
