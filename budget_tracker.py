from tkinter import *
from datetime import datetime
from expenses import Expenses
import calendar

budget = 2000

def main():
    # print("Running Expense Tracker")
    expense_file_path = "expenses.csv"

    # Get user input for expense
    get_user_budget()
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expense(expense_file_path, budget)

def get_user_budget():
    global budget 
    budget = round(float(input("Enter your budget: $")), 2)

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
        f.write(f"{expense.name},{expense.amount:.2f},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing Expenses")
    all_expenses: list[Expenses] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expenses(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category)
            all_expenses.append(line_expense)

    # organize by category. if no match, create a new category
    amount_by_category = {}
    for expense in all_expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expense By Category")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")

    # get the total budget and compare
    total_spent = sum([ex.amount for ex in all_expenses])
    print(f"Total Spent: ${total_spent:.2f}")
    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print("Spening exceeded budget!")
    else:
        print(f"Remaining Budget: ${remaining_budget} left")
    
    # recommend a daily spending on the user based on how much money left they can spend
    dt = datetime.now()
    print(f"Date: {dt.month}, {dt.day}, {dt.year}")
    days_in_month = calendar.monthrange(dt.year, dt.month)[1]
    remaining_days = days_in_month - dt.day
    daily_budget = remaining_budget / remaining_days
    print(green(f"Recommended Spending Per Day: ${daily_budget:.2f}"))

# make important text/data stand out in the terminal
def green(text):
    return f"\033[92m{text}\033[0m"

def login():
    pass

def save_info():
    pass

def find_password():
    pass

# UI Setup
window = Tk()
window.title("Budget Tracker")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
# canvas.config(bg="white", highlightthickness=0)  


def load_new_page():
    window.destroy()

    new_window = Tk()
    new_window.title("Budget Tracker")
    new_window.config(padx=50, pady=50, bg="white")
    
    canvas = Canvas(width=800, height=800)
    canvas.grid(column=1, row=0)
    canvas.config(bg="white", highlightthickness=0) 


username_text = Label(text="Email:")
username_text.grid(column=0, row=1)

password_text = Label(text="Password:")
password_text.grid(column=0, row=2)

username_entry = Entry(width=30)
username_entry.grid(column=1, row=1)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=2)

login_button = Button(text="LOGIN", width=28)
login_button.grid(column=1, row=3)

create_account_button = Button(text="Create New Account", width=28)
create_account_button.grid(column=1, row=4)

forgot_password_button = Button(text="Forgot Password?", width=10)
forgot_password_button.grid(column=2, row=2)

# This will be true when were run this file directly only
if __name__ == "__main__":
    main()

window.mainloop()
