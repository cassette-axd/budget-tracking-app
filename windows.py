# This class will create the windows used for the front end of this application
from tkinter import *
from tkinter import messagebox
import re
import json

#first page to open up where users can sign in to their account
class LoginWindow:
    def __init__(self, master):
        master.config(padx=50, pady=50)
        canvas = Canvas(master, width=200, height=200)
        canvas.grid(column=1, row=0) 

        username_text = Label(text="Username:")
        username_text.grid(column=0, row=1)

        password_text = Label(text="Password:")
        password_text.grid(column=0, row=2)

        self.username = StringVar()
        self.username_entry = Entry(textvariable=self.username, width=30)
        self.username_entry.grid(column=1, row=1)

        self.password = StringVar()
        self.password_entry = Entry(textvariable=self.password, width=30)
        self.password_entry.grid(column=1, row=2)

        login_button = Button(text="LOGIN", width=28, command=self.login)
        login_button.grid(column=1, row=3)

        create_account_button = Button(text="Create New Account", width=28, command=self.create_new_account)
        create_account_button.grid(column=1, row=4)

        forgot_password_button = Button(text="Forgot Password?", width=10)
        forgot_password_button.grid(column=2, row=2)

    def create_new_account(self):
        new_account_window = CreateAccountWindow()

    # try to log the user into their account
    def login(self):
            try:
                with open("data.json", "r") as data_file:
                    # read data
                    data = json.load(data_file)
            except FileNotFoundError:
                messagebox.showinfo(title="Error", message="Error""\nData File not Found")
            else:
                username = self.username_entry.get()
                password = self.password_entry.get()

                # check if website is stored in data
                if self.username_entry.get() == "" or self.password_entry == "":
                    messagebox.showinfo(title="Error", message="Error""\nSome of your entries are blank")
                if username in data:
                    # get the info for that website in the nested dictionary and display it in a popup
                    if data[username]["Password"] == password:
                        messagebox.showinfo(title="Success", message="Login Successful")
                    else:
                        messagebox.showinfo(title="Error", message="Invalid Password")
                else:
                    messagebox.showinfo(title="Error", message="Invalid Username")

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

    def save_info(self):
        stored_accounts = {
            self.username.get(): {
                "Email": self.email.get(),
                "Password":  self.password1.get()
            }
        }
        # store data as a json file
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
        # create a new json data file if it doesn't currently exist
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(stored_accounts, data_file, indent=4)
        else:
            # update old data with new data
            data.update(stored_accounts)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        # clear text boxes regardless of what happens
        finally:
            messagebox.showinfo(title="success", message="Your New Account Has Been Created")
            self.username_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.password_entry_2.delete(0, END)

    def submit(self):
        # first check if account information already exists
        try:
            with open("data.json", "r") as data_file:
                # read data
                data = json.load(data_file)
        except FileNotFoundError:
                pass
        else:
            # check if input is stored in data
            if self.username.get() in data:
                messagebox.showinfo(title="Error", message="Error""\nUsername already exists")
            for user, user_data in data.items():
                if user_data['Email'] == self.email.get():
                    messagebox.showinfo(title="Error", message="Error""\nEmail already exists")
            
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # then check if given ivalid input
        if self.password1.get() != self.password2.get():
            messagebox.showinfo(title="Error", message="Error""\nPasswords don't match")
        elif self.username.get() == "" or self.email.get() == "" or self.password1.get() == "" or self.password2.get() == "":
            messagebox.showinfo(title="Error", message="Error""\nSome of your entries are blank")
        elif str(re.match(regex, self.email.get())) == "None":
            messagebox.showinfo(title="Error", message="Error""\nEmail is invalid")
        else:
            # if all input is valid, store it in a dictionary
            self.save_info()
        
root = Tk()
root.title("Budget Tracker")
main_window = LoginWindow(root)
root.mainloop()
