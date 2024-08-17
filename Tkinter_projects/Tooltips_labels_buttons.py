from tkinter import *
import tkinter as tk

#create the main window
parent = tk.Tk()
parent.title("Tooltip Example")

#Function to show tooltips
def show_tooltip(event, tooltip_text):
    tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")  # Adjust tooltip position
    tooltip_label.config(text=tooltip_text)
    tooltip.deiconify()

#Function to hide tooltips
def hide_tooltip(event):
    tooltip.withdraw()

#Create a button with a tooltip
button = tk.Button(parent, text="Button with Tooltip")
button.pack(padx=10, pady=10)
button.bind("<Enter>", lambda event, text="This is a button.": show_tooltip(event, text))
button.bind("<Leave>", hide_tooltip)

#Create a label with a tooltip
label = tk.Label(parent, text = "Label with Tooltip")
label.pack(padx=10, pady=10)
label.bind("<Enter>", lambda event, text="This is label.": show_tooltip(event,text))
label.bind("<Leave>", hide_tooltip)


#Create a tooltip window(hiiden by default)
tooltip = tk.Toplevel(parent)
tooltip.withdraw()
tooltip_label = tk.Label(tooltip, text="", background="lightyellow", relief="solid", borderwidth=1)
tooltip_label.pack()

#Start the Tkinter event loop
parent.mainloop()