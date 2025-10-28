import streamlit as st
from datetime import datetime
import requests
API_URL = "http://localhost:8000"
import pandas as pd

def month_analytics_tab():
    response = requests.get(f"{API_URL}/analytics/month")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.subheader("Monthly Expenses")
        st.bar_chart(
            data=df.set_index("Month")["Total"],
            use_container_width=True
        )  # 👈 makes your month the X-axis and total the Y-axis
    else:
        st.error("Failed to fetch analytics data.")

