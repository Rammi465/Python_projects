from tkinter import *
import tkinter as tk
import time

#create a main window
parent = tk.Tk()
parent.title("Digital Clock")

#Create a label to display the time
clock_label = tk.Label(parent, text = "", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)

#Function for updating the time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    parent.after(1000, update_time) #update evry 1000 milliseconds

#Start updating the time
update_time()

#start the tkinter 
parent.mainloop()
