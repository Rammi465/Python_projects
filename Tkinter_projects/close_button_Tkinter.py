import tkinter as tk

#Create the main window
parent = tk.Tk()
parent.title("Close window example")

#Function to close the window
def close_window():
    parent.destroy()

#Crete a label
label = tk.Label(parent, text="Click the 'close' button to close the window.")
label.pack(padx=25, pady=25)

#Create the close button
close_button = tk.Button(parent, text="Close", command=close_window)
close_button.pack()

#Start the Tkinter event loop
parent.mainloop()

