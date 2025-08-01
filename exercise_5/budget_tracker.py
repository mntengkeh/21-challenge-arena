monthly_income_expense = {
    "2024-1": {
        "income": {"salary": 2000, "business":5000, "xtra":1500}, 
        "expenses": {
            "food": {"budget": 180, "spent":200},
            "housing":{"budget": 700, "spent":600},
            "transport":{"budget": 600, "spent":400}
        }
    }
}


# outputs general analysis for the month specified
def get_financial_summary():
    print("\n=== PERSONAL BUDGET TRACKER ===\n")
    date = input("Month and year (space separated): ")
    arr = date.split()
    dateKey = f"{arr[1].strip()}-{month_map(arr[0].strip().lower())}"

    target_month = monthly_income_expense[dateKey]

    expenses = target_month["expenses"]

    print("\n💰 FINANCIAL SUMMARY")

    t_income = total_income(target_month["income"])
    t_expenses = total_expenses(expenses)
    net_savings = t_income - t_expenses

    print(f"Total Income: ${t_income:.2f}")
    print(f"Total expenses: ${t_expenses:.2f}")
    print(f"Net savings: ${net_savings:.2f} ({(net_savings/t_income) * 100:.1f}%)")

    print("\n📊 EXPENSE BREAKDOWN")
    for key, value in get_expense_details(t_income, expenses).items():
        print(f"{key}: {value:.2f}%")


    print("\n⚠️ BUDGET ALERTS:")
    for key, value in check_for_alert(target_month["expenses"]).items():
        print(f"{key.capitalize()} expenditure is over budget")

# checks for expense items which have exceeded budget
def check_for_alert(expenses):
    exceeded = {}
    for key, value in expenses.items():
        p_check = (value["spent"] / value["budget"]) * 100
        if p_check > 100:
            exceeded[key] = p_check
    return exceeded

# calculates the percentage of total income spent on each expense item
def get_expense_details(total, expenses):
    i_percentage = {}
    for key, value in expenses.items():
        i_percentage[key] = (value["spent"] / total) * 100
    return i_percentage

# calculates total expenses for a given month
def total_expenses(expenses):
    t_expenses = 0
    for value in expenses.values():
        t_expenses += value["spent"]
    return t_expenses

# calculates total income from all sources
def total_income(income):
    t_income = 0
    for value in income.values():
        t_income += value
    return t_income

# maps month names to numbers
def month_map(month):
    month_number = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
    return month_number[month]




# def add_month_start_data(month, year, budget):
#     m_key = f"{year}-{month_map(month)}"
#     monthly_income_expense[f"{year}"]




get_financial_summary()