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
import json


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

    new_data ={ website: {
            
        "email": email,
        "password": password, 
    }
        }
    
    # control empty field
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Wait", message="Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered:\nURL: {website} \nEmail: {email}"
                                       f"\nPassword: {password} \nSave?")
        if is_ok:
                try:
                    with open("pwd.json", "r") as data_file:
                    #Reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("pwd.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                #Updating old data with new data
                    data.update(new_data)

                    with open("pwd.json", "w") as data_file:
                        #Saving updated data
                        json.dump(data, data_file, indent=4)
                
                finally:
                    url_entry.delete(0, END)
                    password_entry.delete(0, END)
def find_password():
    website = url_entry.get()
    try:
        with open("pwd.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

def stamp():
    if (not os.path.exists('pwd.json')):
        messagebox.showinfo(title='Alert', message='There aren\'t passwords stored')
        return
    #data = pandas.read_json('pwd.json')
    #print(data)
    if (platform.system() == 'Linux'):
        subprocess.run(["xdg-open", "./pwd.json"])
    else:
        # Other System such as windows
        os.system("start .\\pwd.json")


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
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
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
