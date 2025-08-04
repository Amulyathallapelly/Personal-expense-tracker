import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = {}
        self.categories = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.expenses = data.get('expenses', {})
                self.categories = data.get('categories', {})

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump({'expenses': self.expenses, 'categories': self.categories}, file)

    def add_expense(self, date, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append((date, amount))
        self.save_data()

    def add_category(self, category, budget=0):
        if category not in self.categories:
            self.categories[category] = {'budget': budget, 'spent': 0}
            self.save_data()

    def set_budget(self, category, budget):
        if category in self.categories:
            self.categories[category]['budget'] = budget
            self.save_data()

    def view_expenses(self):
        for category, items in self.expenses.items():
            total_amount = sum(amount for _, amount in items)
            print(f"{category}: ${total_amount:.2f}")

    def view_categories(self):
        print("Categories:")
        for category, info in self.categories.items():
            budget = info['budget']
            spent = sum(amount for _, amount in self.expenses.get(category, []))
            print(f"{category} - Budget: ${budget:.2f}, Spent: ${spent:.2f}")

# Sample usage
tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Add Category")
    print("3. Set Category Budget")
    print("4. View Expenses")
    print("5. View Categories")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: $"))
        category = input("Enter category: ")
        tracker.add_expense(date, amount, category)
    elif choice == "2":
        category = input("Enter category: ")
        tracker.add_category(category)
    elif choice == "3":
        category = input("Enter category: ")
        budget = float(input("Enter budget: $"))
        tracker.set_budget(category, budget)
    elif choice == "4":
        tracker.view_expenses()
    elif choice == "5":
        tracker.view_categories()
    elif choice == "6":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
