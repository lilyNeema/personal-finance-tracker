import matplotlib.pyplot as plt

def plot_expenses(expenses):
    categories = [exp["category"] for exp in expenses]
    amounts = [exp["amount"] for exp in expenses]
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='orange')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def plot_income_vs_expenses(income, expenses):
    total_income = sum(inc["amount"] for inc in income)
    total_expenses = sum(exp["amount"] for exp in expenses)
    labels = ['Income', 'Expenses']
    amounts = [total_income, total_expenses]
    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
    plt.title("Income vs Expenses")
    plt.show()
