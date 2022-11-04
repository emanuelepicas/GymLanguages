#!/bin/python3

from tkinter import *
from tkinter import messagebox
import pandas
import os
import subprocess
import platform
from random import choice, randint, shuffle
import pyperclip
import sys 


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = url_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # control empty field
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Wait", message="Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered:\nURL: {website} \nEmail: {email}"
                                       f"\nPassword: {password} \nSave?")
        if is_ok:
            with open("pwd.csv", "a") as data_file:
                if (os.path.getsize('pwd.csv') == 0):
                    data_file.write("URL,Email,Password\n")
                data_file.write(f"{website},{email},{password}\n")
                url_entry.delete(0, END)
                #email_entry.delete(0, END)
                password_entry.delete(0, END)
#Trying to output correctly the table as is printed in the stdout TODO
# def redirector(inputStr):
#   messagebox.showinfo(title="sample",message=inputStr)  

# sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.


def stamp():
    if (not os.path.exists('pwd.csv')):
        messagebox.showinfo(title='Alert', message='There aren\'t passwords stored')
        return
    data = pandas.read_csv('pwd.csv')
    print(data)
    if (platform.system() == 'Linux'):
        subprocess.run(["xdg-open", "./pwd.csv"])
    else:
        # Other System such as windows
        os.system("start .\\pwd.csv")


window = Tk()
# setting the image position
window.title("Password Manager")
window.config(padx=10, pady=10)
#textbox=Text(window)

canvas = Canvas(height=400, width=400)
logo = PhotoImage(file="lock.png")
canvas.create_image(200, 189, image=logo)
canvas.grid(row=0, column=1)
# canvas.pack()

# Creating Labels

url_label = Label(text='URL')
url_label.grid(row=1, column=0)
email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)
password_label = Label(text='Password')
password_label.grid(row=3, column=0)

url_entry = Entry(width=35)
url_entry.grid(row=1, column=1)
# focus the cursor at the url entry
url_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
# EmailPlaceholder
email_entry.insert(0, "sample@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Setting Button
generate_password_button = Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
# event listener for the function to use
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1)

# Show password
show_password = Button(text="Show All Passwords Stored", command=stamp)
show_password.grid(row=5, column=1)

window.mainloop()
