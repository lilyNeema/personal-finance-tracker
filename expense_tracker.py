expenses = []

def add_expense(category, amount):
    expenses.append({"category": category, "amount": amount})
    print(f"Added expense: {amount} in {category}.")

def get_expenses():
    return expenses
