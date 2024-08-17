import tkinter as tk
from tkinter import messagebox

#Create a mainwinow
parent = tk.Tk()
parent.title("Login Form")


#Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

  # Validation logic
    if userid == "admin" and password == "password":
      messagebox.showinfo("Login successful", "Welcome, Admin!")
    else:
     messagebox.showerror("Login Failed", "Invalid username and password")

#Create and place the username label and entry

username_label = tk.Label(parent, text="userid: ")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()


#Ceate and place the password label and entry

password_label = tk.Label(parent, text="Password: ")
password_label.pack()

password_entry = tk.Entry(parent, show="*") #show asterisks for password
password_entry.pack()

#Create and place the login button
login_button = tk.Button(parent, text="Login", command= validate_login)
login_button.pack()

#

#Satrt the Tkinter event loop
parent.mainloop()