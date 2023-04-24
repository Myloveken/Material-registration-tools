import tkinter as tk
from tkinter import ttk
import datetime  as dt

list_type = ['box', 'livre', 'ounce',]
list_codes = []
windows = tk.Tk()

#function create
def insert_code():
    description=entry_description.get()
    type=combobox_selectionary_type.get()
    quant= entry_quant.get()
    date_create = dt.datetime.now()
    date_create = date_create.strftime("%d/%m/%Y, %H:%M:%S")
    code=len(list_codes)+1
    code_str = "code".format(code)
    list_codes.append((code_str, description, type, quant, date_create))

#windows title

windows.title("Material Registration Tools")

label_description = tk.Label(text="Material Description")
label_description.grid(row=1, column=0, padx=10, pady= 10, sticky="nse", columnspan = 4)

entry_description = tk.Entry()
entry_description.grid(row=2, column=0, padx=10, sticky="nse", columnspan= 4)

label_unit_type = tk.Label(text="Material Unit-Type")
label_unit_type.grid(row=3, column=0, padx= 10, pady=10, sticky="nse",columnspan=2)

combobox_selectionary_type = ttk.Combobox(values=list_type)
combobox_selectionary_type.grid(row=3, column=2, padx=10, pady=10, sticky="nse", columnspan=2)

label_quant = tk.Label(text ="Quantity Material Unit-Type")
label_quant.grid(row=4, column=0, padx= 10, pady=10, sticky="nse", columnspan=2)


entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx= 10, pady=10, sticky="nse", columnspan=2)

button_create_code = tk.Button(text="create code", command= insert_code())
button_create_code.grid(row=5, column=2, padx= 10, pady=10, sticky="nse", columnspan=2)

windows.mainloop()

print(list_codes)