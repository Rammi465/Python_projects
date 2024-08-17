from tkinter import *
import tkinter as tk

#creat a mainwindow

root = tk.Tk()
root.title("Temperature Converter")


#Function to convert from celsius to Faranheit

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

    except ValueError:
        result_label.config(text="Invalid input")

    
#Function to convert from Faranheit to Celsius
    
def fahrenheit_to_celsius():
    try:
       fahrenheit = float(fahrenheit_entry.get())
       celsius = (fahrenheit - 32) * 5/9;
       result_label.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Invalid input")

#Celsius to Fahrenheit conversion
celsius_label = tk.Label(root, text="Input Celsisus:")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(root)
celsius_entry.grid(row=0, column=1)

c_to_f_button = tk.Button(root, text="Convert to Faranheit", command = celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=2)


#Fahrenheit to Celsius conversion

fahrenheit_label = tk.Label(root, text = "Input Fahrenheit:")
fahrenheit_label.grid(row=1, column=0)

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=1)

f_to_c_button = tk.Button(root, text="Convert to Celsius", command = fahrenheit_to_celsius)
f_to_c_button.grid(row=1, column=2)

#Display the result

result_label = tk.Label(root, text="", font = ("Helvetica", 14))
result_label.grid(row=2, columnspan=3)

#Start the vent loop
root.mainloop()









