import tkinter as tk
from tkinter import ttk
import datetime  as dt

windows = tk.Tk()

#windows title

windows.title("material registration tools")

label_descreption = tk.Label(text="Material Description")
label_descreption.grid(row=1, column=0, padx=10, pady= 10, sticky="nse", columnspan = 4)

entry_description = tk.Entry()
entry_description.grid(row=2, column=0, padx=10, sticky="nse", columnspan= 1)

windows.mainloop()
