Expense Tracker (FastAPI + MySQL + Streamlit)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.120-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


A full-stack expense tracking system built with FastAPI, MySQL, and Streamlit, enabling users to add, view, and analyze their daily expenses with real-time data visualization.

Project Overview

This project provides an interactive dashboard for tracking and analyzing daily expenses.
Users can log expenses, view summaries by category and date range, and visualize their spending trends with real-time charts powered by Pandas and Streamlit.

Tech Stack
Layer	                            Technology
Frontend	                        Streamlit
Backend                             API	FastAPI
Database	                           MySQL
ORM/Connector	            mysql-connector-python
Visualization	                   Pandas, Altair
Testing	                                Pytest
Server	                                Uvicorn

🧩 Features

✨ Expense CRUD — Add, update, and view daily expenses
📆 Date-based Filtering — Retrieve spending history for any given date
📈 Visual Analytics — Dynamic bar charts & category percentage breakdown
🧮 Aggregated Insights — Automatic grouping and total computation via SQL
⚡ Modern API Design — REST endpoints ready for integration
🧱 Modular Architecture — Separate layers for backend, frontend, and data logic
💾 Persistent Storage — MySQL keeps all records structured and query-ready
🎨 Clean UI — Streamlit components arranged in column-based layout for clarity

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
