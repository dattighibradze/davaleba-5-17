import tkinter as tk

def calculate_sum():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        result.set("Please enter valid numbers")

root = tk.Tk()
root.title("Sum Calculator")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=10, pady=10)

result = tk.StringVar()
sum_label = tk.Label(root, textvariable=result)
sum_label.grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(root, text="Calculate", command=calculate_sum).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
