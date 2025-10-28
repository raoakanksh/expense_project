Expense Tracker (FastAPI + MySQL + Streamlit)

A full-stack expense tracking system built with FastAPI, MySQL, and Streamlit, enabling users to add, view, and analyze their daily expenses with real-time data visualization.

Project Overview

This project allows users to:

Add and update expenses by category and date

Retrieve expenses from a MySQL database through FastAPI endpoints

View summarized analytics (total per category, percentage breakdowns, etc.)

Visualize data using Streamlit’s interactive dashboard and charts

Tech Stack
Layer	                            Technology
Frontend	                        Streamlit
Backend                             API	FastAPI
Database	                           MySQL
ORM/Connector	            mysql-connector-python
Visualization	                   Pandas, Altair
Testing	                                Pytest
Server	                                Uvicorn

Project Structure:
expense_project/
│
├── backend/
│   ├── db_helper.py          # Handles MySQL queries and CRUD operations
│   ├── main.py               # FastAPI endpoints for expenses and analytics
│   └── logging.py            # Custom logger setup
│
├── frontend/
│   ├── app.py                # Streamlit app for UI interaction
│   └── analytics.py          # Streamlit analytics visualization
│
├── tests/
│   ├── backend/
│   │   └── test_db_helper.py # Unit tests for database helper functions
│   └── conftest.py           # Shared pytest configurations
│
├── requirements.txt
└── README.md


Setup Instructions
1) Clone the Repository
git clone https://github.com/raoakanksh/expense_project.git
cd expense_project

2) Create A virtual Enviornment
python3 -m venv venv
source venv/bin/activate

3) Install Dependencies
pip install -r requirements.txt

4) Configure MySQL
CREATE DATABASE expense_manager;
USE expense_manager;

5) Run FastAPI Backend
cd backend
uvicorn main:app --reload

6)Run Streamlit Frontend
cd ../frontend
streamlit run app.py

Features

✅ Add, update, and delete expense records
✅ Fetch all expenses or filter by specific date range
✅ Display category-wise analytics (sum & percentage)
✅ Visualize expenses with interactive bar charts
✅ Backend-Frontend integration using REST APIs


Testing
Run tests with: 
pytest

Future Enhancements

Add authentication (JWT-based login)

Include monthly/weekly breakdown charts

Export reports as CSV or PDF

Deploy backend and frontend to cloud (AWS / Render / Railway)

Author

Akanksh Rao
Purdue University – Computer Engineering
🔗 LinkedIn

💻 GitHub
