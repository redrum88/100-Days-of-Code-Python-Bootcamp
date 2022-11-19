from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    rand_password = ""
    for char in password_list:
        rand_password += char

    password_entry.delete(0, END)
    password_entry.insert(END, string=f"{rand_password}")
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website_entry.get()) < 3:
        messagebox.showerror(title="Missing website.", message="You have not entered website.")
    if len(email_entry.get()) < 5:
        messagebox.showerror(title="Missing email.", message="You have not entered email.")
    if len(password_entry.get()) < 8:
        messagebox.showerror(title="Bad password.", message="Password is too short..")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:

            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File 'data.json' Has Not Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{website}' exist.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic, anchor="center")
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row=1)

website_entry = Entry(width=32)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)
website_entry.focus()

websearch_button = Button(text="Search", command=search, width=11)
websearch_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(column=0, row=2)

email_entry = Entry(width=46)
email_entry.insert(0, string="your@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password", bg=YELLOW)
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Pass", command=generate)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
