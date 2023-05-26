'''a Python program that allows users to track their expenses.
The program provide functionality to add, delete, and categorize
expenses, as well as generate reports or visualizations of spending habits.'''

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def delete_expense(self, expense):
        if expense in self.expenses:
            self.expenses.remove(expense)
        else:
            print("Expense not found.")

    def categorize_expense(self, expense, category):
        expense.category = category

    def generate_report(self):
        total_expenses = len(self.expenses)
        print(f"Total Expenses: {total_expenses}")
        print("Expense Details:")
        for expense in self.expenses:
            print(f"- {expense.name}: {expense.amount} ({expense.category})")


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.category = None


# Example usage:
expense_tracker = ExpenseTracker()
expense1 = Expense("Groceries", 50)
expense2 = Expense("Utilities", 100)
expense3 = Expense("Dining Out", 30)

expense_tracker.add_expense(expense1)
expense_tracker.add_expense(expense2)
expense_tracker.add_expense(expense3)

expense_tracker.categorize_expense(expense1, "Food")
expense_tracker.categorize_expense(expense2, "Bills")
expense_tracker.categorize_expense(expense3, "Food")

expense_tracker.generate_report()
