# This class will create the windows used for the front end of this application
from tkinter import *
from tkinter import messagebox
import re

#first page to open up where users can sign in to their account
class LoginWindow:
    def __init__(self, master):
        master.config(padx=50, pady=50)
        canvas = Canvas(master, width=200, height=200)
        canvas.grid(column=1, row=0) 

        email_text = Label(text="Email:")
        email_text.grid(column=0, row=1)

        password_text = Label(text="Password:")
        password_text.grid(column=0, row=2)

        username_entry = Entry(width=30)
        username_entry.grid(column=1, row=1)

        password_entry = Entry(width=30)
        password_entry.grid(column=1, row=2)

        login_button = Button(text="LOGIN", width=28)
        login_button.grid(column=1, row=3)

        create_account_button = Button(text="Create New Account", width=28, command=self.create_new_account)
        create_account_button.grid(column=1, row=4)

        forgot_password_button = Button(text="Forgot Password?", width=10)
        forgot_password_button.grid(column=2, row=2)

    def create_new_account(self):
        new_account_window = CreateAccountWindow()

# Open a new window for user to create a new account
class CreateAccountWindow:
    import re
    def __init__(self):
        top = Toplevel()
        canvas = Canvas(top, width=200, height=200)
        canvas.grid(column=1, row=0) 

        username_text = Label(top, text="Enter Username:")
        username_text.grid(column=0, row=1)
        
        email_text = Label(top, text="Enter Email:")
        email_text.grid(column=0, row=2)

        password_text = Label(top, text="Enter Password:")
        password_text.grid(column=0, row=3)

        password_text_2 = Label(top, text="Re-Enter Password:")
        password_text_2.grid(column=0, row=4)

        self.username = StringVar()
        self.username_entry = Entry(top, textvariable=self.username, width=30)
        self.username_entry.grid(column=1, row=1)

        self.email = StringVar()
        self.email_entry = Entry(top, textvariable=self.email, width=30)
        self.email_entry.grid(column=1, row=2)

        self.password1 = StringVar()
        self.password_entry = Entry(top, textvariable=self.password1, width=30)
        self.password_entry.grid(column=1, row=3)

        self.password2 = StringVar()
        self.password_entry_2 = Entry(top, textvariable=self.password2, width=30)
        self.password_entry_2.grid(column=1, row=4)

        save_info_button = Button(top, text="Create Account", width=28, command=self.submit)
        save_info_button.grid(column=1, row=5)

    def submit(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # first check if given ivalid input
        if self.password1.get() != self.password2.get():
            messagebox.showinfo(title="Error", message="Error""\nPasswords don't match")
        elif self.username.get() == "" or self.email.get() == "" or self.password1.get() == "" or self.password2.get() == "":
            messagebox.showinfo(title="Error", message="Error""\nSome of your entries are blank")
        elif str(re.match(regex, self.email.get())) == "None":
            messagebox.showinfo(title="Error", message="Error""\nEmail is invalid")
        else:
            # if all input is valid, store it in a dictionary
            print("All input is valid")
        
root = Tk()
root.title("Budget Tracker")
main_window = LoginWindow(root)
root.mainloop()
