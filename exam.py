import string
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import *
window = Tk()

window.geometry("1000x800")

fn = Label(window, text = "First Name: ")
fn.pack()

fn_i = Entry(window, width=30)
fn_i.pack()

ln = Label(window, text = "Last Name: ")
ln.pack()

ln_i = Entry(window, width=30)
ln_i.pack()

gender = Label(window, text = "Gender")
gender.pack()
gender_m = Radiobutton(window, text = '  Male  ', value=1)
gender_f = Radiobutton(window, text = 'Female', value=0)
gender_f.pack()
gender_m.pack()

chk = BooleanVar()
chk.set(True)
chk = Checkbutton(window, text='English', var=chk)
chk.pack()

chk1 = BooleanVar()
chk1.set(False)
chk1 = Checkbutton(window, text='  Hindi', var=chk1)
chk1.pack()

chk2 = BooleanVar()
chk2.set(False)
chk2 = Checkbutton(window, text='Telegu', var=chk2)
chk2.pack()

email_name = Label(window, text = "Email: ")
email_name.pack()

email_i = Entry(window, width=30)
email_i.pack()

address_name = Label(window, text = "Address ")
address_name.pack()

address_i = scrolledtext.ScrolledText(window, width=20, height=5)
address_i.pack()

state_name = Label(window, text = "State ")
state_name.pack()

state_i = Combobox(window)
state_i['values'] = ("Select your option", "Gujarat", "West Bengal")
state_i.current(0)
state_i.pack()

zip_name = Label(window, text = "Zip ")
zip_name.pack()

zip_i = Entry(window, width=20)
zip_i.pack()

credit_name = Label(window, text = "Credit Card Type ")
credit_name.pack()

credit_i = Combobox(window)
credit_i['values'] = ("Select your Credit Card Type", "Visa", "Rupay", "Master Card")
credit_i.current(0)
credit_i.pack()

def submit():
    s = True
    first_name = fn_i.get()
    last_name = ln_i.get()
    state_value = state_i.grab_current()
    state = state_i[state_value]
    zip = zip_i.get()
    credit_value = credit_i.grab_current()
    credit = credit_i[credit_value]
    if(gender_f.getboolean(s) == True):
        gender = "Female"
    else:
        gender = "Male"
    email = str(email_i.get())
    if(email.find("@") == -1):
        messagebox.showinfo("Error 300", "Enter a Valid Email ID")
    else:
        messagebox.showinfo("Succesful", "Data has been store successfully")

def theme() :
    messagebox.showinfo("Theme Change", "Theme Changed Successfully")

def delete():
    messagebox.askyesno("Data Deletion","Are you sure you want to delete the data? ")

insert = Button(window,text = "Submit", command = submit)
insert.pack()

theme = Button(window, text = "Theme", command = theme)
theme.pack()

delete = Button(window, text = "Delete", command = delete)
delete.pack()

s = True
first_name = fn_i.get()
last_name = ln_i.get()
state_value = state_i.grab_current()
state = state_i[state_value]
zip = zip_i.get()
credit_value = credit_i.current()
credit = str(credit_i[credit_value])
if(gender_f.getboolean(s) == True):
    gender = "Female"
else:
    gender = "Male"
email = str(email_i.get())

print(first_name)
print(last_name)
print(state)
print(zip)
print(credit)
print(gender)

window.mainloop()