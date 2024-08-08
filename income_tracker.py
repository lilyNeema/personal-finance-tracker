income = []

def add_income(source, amount):
    income.append({"source": source, "amount": amount})
    print(f"Added income: {amount} from {source}.")

def get_income():
    return income
