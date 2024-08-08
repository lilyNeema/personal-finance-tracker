budget = {
    "food": 300,
    "transportation": 150,
    "entertainment": 100
}

def check_budget():
    total_expenses = sum(exp["amount"] for exp in expenses)
    print(f"Total expenses: {total_expenses}")

    for category, limit in budget.items():
        spent = sum(exp["amount"] for exp in expenses if exp["category"] == category)
        print(f"{category.capitalize()} - Spent: {spent}, Budget: {limit}")
        if spent > limit:
            print(f"Warning: You've exceeded the budget for {category}!")
