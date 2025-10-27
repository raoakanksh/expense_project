#talk to the database and get the records and do the crud operations...
import mysql.connector
import os
from contextlib import contextmanager
from dotenv import load_dotenv


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
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_between_dates(expense_date1, expense_date2):
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

if __name__ == "__main__":
    print("Expenses for August 4th")
    fetch_expenses_between_dates("2024-08-01", "2024-08-05")
