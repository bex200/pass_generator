from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for char in range(randint(8,10))]
    password_list.extend([choice(numbers) for char in range(randint(2,4))])
    password_list.extend([choice(symbols) for char in range(randint(2,4))])
    shuffle(password_list)
    pswrd = "".join(password_list)
    password_entry.insert(0,string= f"{pswrd}")
    pyperclip.copy(pswrd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = web_entry.get()
    password_get = password_entry.get()
    email_get = email_entry.get()
    new_data = {
        web:{
            "email": email_get,
            "password": password_get
            }
        }
    if len(web) == 0 or len(password_get) == 0:
        messagebox.showerror(title="Unfilled data", message="You did not enter required data.")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as new_file:
                json.dump(new_data, new_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH ENGINE ------------------------------- #
def search_website():
    web = web_entry.get()
    try:
        with open("data.json",'r') as opened_file:
            data = json.load(opened_file)
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="No data found")
    else:
        if web in data:
            messagebox.showinfo(title=f"{web}", message=f"Email: {data[web]["email"]}\nPassword: {data[web]["password"]}")
        else:
            messagebox.showerror(title="Not Found", message=f"No information found for {web}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password generator")
window.config(pady=50, padx = 50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo)
canvas.grid(row=0,column=1)

#Labels
www_title = Label(text="Website:")
www_title.grid(row=1, column = 0)

username = Label(text="Email/Username:")
username.grid(row=2, column = 0)

password = Label(text="Password:")
password.grid(row=3, column = 0)

#Entries
web_entry = Entry()
web_entry.grid(column=1,row= 1, sticky="EW")
web_entry.focus()

email_entry = Entry()
email_entry.grid(column=1,row= 2, columnspan = 2, sticky="EW")
email_entry.insert(0,"example@test.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row = 3, column =2, sticky="EW")

add_button = Button(text="Add",command = save_data)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = "EW" )

search_button = Button(text="Search", command=search_website)
search_button.grid(column = 2, row = 1, sticky = "EW")

window.mainloop()