from tkinter import *
from datetime import datetime
from expenses import Expenses

# get the current time
dt = datetime.now()
# get the current day
current_day = dt.strftime('%A')
#print(current_day)

max_budget = 0
money_spent = 0

def main():
    print("Running Expense Tracker")

    # Get user input for expense
    expense = get_user_expense()
    expense_file_path = "expenses.csv"

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expense(expense_file_path)

def get_user_expense():
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: $"))
            expense_amount = round(expense_amount, 2)
            break
        except Exception:
            print("Invalid Value")
    #print(f"You've entered {expense_name} and ${expense_amount}")

    expense_categories = ["Food", "Groceries", "Bills", "Fun", "Other"]

    while True:
        for i, category_name in enumerate(expense_categories):
            print(f"    {i+1}. {category_name}")
        try:
            index = int(input("Select Category of Expense: ")) - 1
            if (index in range(len(expense_categories))):
                category = expense_categories[index]
                new_expense = Expenses(expense_name, category, expense_amount)
                return new_expense
            else:
                print("Invalid Index")
        except Exception:
            print("Please enter a number")


def save_expense_to_file(expense: Expenses, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, ${expense.amount:.2f}, {expense.category}\n")

def summarize_expense(expense_file_path):
    print("Summarizing Expenses")
    all_expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)


# UI Setup
# window = Tk()
# window.title("Budget Tracker")
# window.config(padx=50, pady=50, bg="white")

#canvas = Canvas(width=800, height=800)
#canvas.grid(row=0,column=0, columnspan=2)
#canvas.config(bg="white", highlightthickness=0)

# This will be true when were run this file directly only
if __name__ == "__main__":
    main()


#window.mainloop()