from random import random, choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    num_let = [choice(letters) for _ in range(nr_letters)]
    num_symbl = [choice(symbols) for _ in range(nr_symbols)]
    num_num = [choice(numbers) for _ in range(nr_numbers)]

    password_list = num_let + num_symbl + num_num

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    name_save = name_entry.get()
    email_save = email_entry.get()
    password_save = password_entry.get()

    new_data = {
        name_save: {
            'email': email_save,
            'password': password_save,
        }
    }

    if len(name_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title='OOOpppsss', message='Please make sure you have not left any fields empty!!')

    else:
        try:
            with open('data.json', 'r') as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        else:

            #updating old data with new one
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
        # is_ok = messagebox.askokcancel(title='website', message=f'There are the details entered:\n {email_save}'
        #                                                  f'\nPassword: {password_save}\n Is it ok to save ?')
        #
        # if is_ok:
        #     with open('data_saved.txt', 'a') as data_file:
        #         data_file.write(f'{name_save} | {email_save} | {password_save} \n')
            name_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- Find Password ------------------------------- #

def find_password():
    name = name_entry.get().capitalize()


    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Fatal Error",
                            message='There is no any information about This Article!!')
    else:

        if name in data:
            email = data[name]['email']
            password = data[name]['password']

            messagebox.showinfo(title=name, message=f'This is the what you searching on the Database \nEmail: {email}\n '
                                                    f'Password: {password}')

        else:
            messagebox.showinfo(title=name,
                                message='There is no any information about This Article!!')





# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title('Password Generator')
windows.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)

created_image = PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=created_image)
canvas.grid(column=1, row=0)


#labels

name = Label(text='Full Name:')
name.grid(column=0, row=2)

email = Label(text='Email:')
email.grid(column=0, row=3)

password = Label(text='Password:')
password.grid(column=0, row=4)


#Entries

name_entry = Entry(width=32)
name_entry.grid(row=2, column=1)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, 'hasan9091.fs@gmail.com')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=4)


#Buttons

generate_password_Btn = Button(text='Generate Password', command=generate_password)
generate_password_Btn.grid(column=2, row=4)

add_Btn = Button(text='add', width=42, command=save)
add_Btn.grid(column=1, row=5, columnspan=2)

search_Btn = Button(text='Search', width=13, command=find_password)
search_Btn .grid(column=2, row=2)






windows.mainloop()
