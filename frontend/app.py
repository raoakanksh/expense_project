import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"
st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1))
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        expenses_available = response.json()
        #st.write(expenses_available)
    else:
        st.error("Failed to get expenses")
        expenses_available = []

    #now lets create a table format so the data recieved from the backend can sit nicely in the table
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    updated_expense = []

    with st.form(key='expenses_form'):
        for i in range(5):
            #if the specified date has up to 5 items then do this.. otherwise set the default value to 0...
            if i < len(expenses_available):
                amount = expenses_available[i]["amount"]
                category = expenses_available[i]["category"]
                notes = expenses_available[i]["notes"]

            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                if i == 0:
                    st.markdown("Amount")
                amount_input = st.number_input("Amount", min_value=0.0, step= 1.0, value = float(amount), key=f"amount_{selected_date}_{i}", label_visibility="collapsed")
            with col2:
                if i == 0:
                    st.markdown("Category")
                    # since its a dropdown... this will return the index of where in the dropdown the specified category is.. -> index = categories.index(category)
                category_input = st.selectbox("Category", options = categories, index = categories.index(category), key=f"category_{selected_date}_{i}", label_visibility="collapsed" )
            with col3:
                if i == 0:
                    st.markdown("Notes")
                notes_input = st.text_input("Notes",  value = notes, key=f"note_{selected_date}_{i}", label_visibility="collapsed")

            updated_expense.append({
            "amount": amount_input,
            "category": category_input,
            "notes": notes_input,
            })

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            #now some default values may be 0 so we do not want to append this to the database...
            filtered_expenses = [expense for expense in updated_expense if expense["amount"] > 0]
            requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if(response.status_code == 200):
                st.success("Successfully updated expenses")
            else:
                st.error("Failed to update expenses")
