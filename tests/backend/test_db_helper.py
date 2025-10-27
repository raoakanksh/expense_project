from backend import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-09-05")
    assert len(expenses) == 6
    assert expenses[0]["amount"] == 350
    assert expenses[0]["category"] == "Rent"


def test_insert_expense():
    db_helper.insert_expense("2025-10-27", 99.99, "TestCategory", "pytest insert")
    expenses = db_helper.fetch_expenses_for_date("2025-10-27")
    assert any(e["notes"] == "pytest insert" for e in expenses)
    assert any(e["amount"] == 99.99 for e in expenses)

def test_percentage_calculation_between_dates():
    data = db_helper.fetch_expenses_between_dates("2024-09-01", "2024-09-05")
    total_percentage = sum([e["Percentage"] for e in data])
    assert round(total_percentage) == 100  # Should sum up to ~100%
    for e in data:
        assert 0 <= e["Percentage"] <= 100

def test_fetch_expenses_between_dates():
    expenses_summary = db_helper.fetch_expenses_between_dates("2024-09-01", "2024-09-05")
    assert isinstance(expenses_summary, list)
    categories = [e["Category"] for e in expenses_summary]
    assert "Food" in categories
    assert "Rent" in categories
    assert all("Total" in e for e in expenses_summary)
    # Example sanity check: Rent should be > 0
    rent_total = next((e["Total"] for e in expenses_summary if e["Category"] == "Rent"), None)
    assert rent_total is not None
    assert rent_total > 0

def test_fetch_expenses_for_date_multiple_results():
    expenses = db_helper.fetch_expenses_for_date("2024-09-05")
    assert all(e["expense_date"].strftime("%Y-%m-%d") == "2024-09-05" for e in expenses)
    assert any(e["category"] == "Food" for e in expenses)
    assert any(e["amount"] == 15.75 for e in expenses)


