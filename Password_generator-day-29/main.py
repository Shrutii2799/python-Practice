from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    password_number=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list =password_number+password_symbol+password_letter
    # print(password_list)

    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password )

#-----------------------------FIND PASSWORD---------------------------------#
def find_password():
    website=website_entry.get()

    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="no data file found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="no data file found")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website= website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{"email":email,"password": password }    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Opps",message="Please make sure you haven't left any field empty. ")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
                print(data)  # Now you will see the dictionary in console


        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)#updating old data with new data

            with open("data.json", "w") as data_file:
                 json.dump(data,data_file,indent=4) #saving updated data

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(pady=50,padx=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(140,100,image=logo_img)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="password:")
password_label.grid(column=0,row=3)

#entries
website_entry=Entry(width=36)
website_entry.grid(row=1,column=1,columnspan=36,sticky="w" ,padx=5, pady=5)
website_entry.focus()
email_entry=Entry(width=54)
email_entry.grid(row=2,column=1,columnspan=3,sticky="w", padx=5, pady=5)
email_entry.insert(0,"shrutimutyal@gmail.com")
password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,sticky="e", padx=5, pady=5)

#button
search_button=Button(text="Search",width=12,command=find_password)
search_button.grid(row=1,column=2)
generate_password_button=Button(text="Generate Password",width=14,command=generate_password)
generate_password_button.grid(column=2,row=3, padx=5, pady=5)
add_button=Button(text="Add",width=46,command= save)
add_button.grid(row=4,column=1,columnspan=3, padx=5, pady=5)

window.mainloop()