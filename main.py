from expense_tracker import add_expense, get_expenses
from income_tracker import add_income, get_income
from budget_tracker import check_budget
from visualization import plot_expenses, plot_income_vs_expenses

def main():
    print("Welcome to the Personal Finance Tracker!")

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. View Income")
        print("5. Check Budget")
        print("6. Visualize Data")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(category, amount)
        elif choice == '2':
            source = input("Enter income source: ")
            amount = float(input("Enter income amount: "))
            add_income(source, amount)
        elif choice == '3':
            expenses = get_expenses()
            print("Expenses:", expenses)
        elif choice == '4':
            income = get_income()
            print("Income:", income)
        elif choice == '5':
            check_budget()
        elif choice == '6':
            plot_expenses()
            plot_income_vs_expenses()
        elif choice == '7':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
