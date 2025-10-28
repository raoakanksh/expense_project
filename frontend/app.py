import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from add_update import add_update_tab
from analytics import add_analytics_tab
from month_analytics import month_analytics_tab

API_URL = "http://localhost:8000"
st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Overall Analytics", "Monthly Analytics"])

with tab1:
    add_update_tab()

with tab2:
    add_analytics_tab()

with tab3:
    month_analytics_tab()




#now time for second tab analytics...



