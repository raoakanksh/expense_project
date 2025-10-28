#talk to the database and get the records and do the crud operations...
import mysql.connector
import os
from contextlib import contextmanager
from dotenv import load_dotenv
from logging_utils import setup_logger

logger = setup_logger('db_helper')


load_dotenv()

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASS", ""),  # read from env
        database=os.environ.get("DB_NAME", "expense_manager")
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    logger.debug("Fetching all records called...")
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date called with... : {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
    return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense for date called with... : {expense_date}, amount : {amount}, category : {category}, notes : {notes}")
    with get_db_cursor(commit = True) as cursor:
        query = "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (expense_date, amount, category, notes))

def fetch_expenses_between_dates(expense_date1, expense_date2):
    logger.info("Fetching expenses between dates {expense_date1} and {expense_date2} called...")
    query = ("SELECT category as Category, SUM(amount) as Total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category ORDER BY category")

    with get_db_cursor() as cursor:
        cursor.execute(query, (expense_date1, expense_date2))
        expenses_between_dates = cursor.fetchall()
        sum = 0
        for total in expenses_between_dates:
                sum +=  total["Total"]#150...

        for percentage in expenses_between_dates:
            percentage["Percentage"] = round(percentage["Total"] / sum * 100, 2)

        print(" --------")
        for expense in expenses_between_dates:
            print(expense)

    return expenses_between_dates

def delete_expenses(expense_date):
    logger.info(f"Deleting expenses for date called with ...: {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        query = "DELETE FROM expenses WHERE expense_date = (%s)"
        cursor.execute(query, (expense_date,))


if __name__ == "__main__":
   print("fetch october 10")
   fetch_expenses_for_date("2025-10-10")



