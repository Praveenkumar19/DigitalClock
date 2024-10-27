# Importing Modules
from tkinter import *
from time import strftime

root = Tk()  # Creates tkinter window
root.title("Digital Computer Clock")  # Adds title to tkinter window

def time():
    string = strftime("%H:%M:%S %p")  # Format for time
    date_string = strftime("%A, %B %d, %Y")  # Format for date
    lbl.config(text = f"{string}\n{date_string}")  # Update label with time and date
    lbl.after(1000, time)  # Refresh every second

# Styling the label widget which displays the clock
lbl = Label(root, font=("arial", 60, "bold"), bg="black", fg="white")  # Adjust font size

# Pack method in tkinter packs widgets into rows or columns. Positions label
lbl.pack(anchor="center", fill="both", expand=1)

time()  # Time function is called

mainloop()  # Runs the application program
