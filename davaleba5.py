import tkinter as tk
from tkinter import ttk
import calendar

def display_calendar():
    year = int(year_entry.get())
    month = int(month_combobox.get())
    calendar_label.config(text=calendar.month(year, month))

root = tk.Tk()
root.title("Calendar Application")

year_entry = ttk.Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(root, text="Enter Year:").grid(row=0, column=0, padx=5, pady=5, sticky="e")

month_combobox = ttk.Combobox(root, values=list(range(1, 13)), state="readonly")
month_combobox.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(root, text="Select Month:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
month_combobox.current(0)

ttk.Button(root, text="Display Calendar", command=display_calendar).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

calendar_label = ttk.Label(root)
calendar_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
