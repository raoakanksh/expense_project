from fastapi import FastAPI
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class AnalyticsRequest(BaseModel):
    expense_date1: date
    expense_date2: date

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model = List[Expense]) #this specifies that i only want to get a list of whatever is in class expenses
def get_expenses(expense_date:date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def create_or_update(expense_date: date, expenses : List[Expense]):
    db_helper.delete_expenses(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expense added successfully"}

@app.post("/analytics")
def get_analytics(request: AnalyticsRequest):
    analytics = db_helper.fetch_expenses_between_dates(request.expense_date1, request.expense_date2)
    return analytics



