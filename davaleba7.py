import tkinter as tk

def update_label():
    selected_options = [option_text.get() for option_text, checkbox_var in zip(option_texts, checkbox_vars) if checkbox_var.get() == 1]
    display_label.config(text=", ".join(selected_options))

root = tk.Tk()
root.title("Checkbox Display")

options = ["არჩვანი 1", "არჩევანი 2", "არჩევანი 3"]

checkbox_vars = []
option_texts = []

for option in options:
    var = tk.IntVar()
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(root, text=option, variable=var, command=update_label)
    checkbox.pack(anchor=tk.W)
    option_texts.append(tk.StringVar(value=option))

display_label = tk.Label(root, text="")
display_label.pack(pady=10)

root.mainloop()
