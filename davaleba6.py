import tkinter as tk

def display_text():
    text = text_entry.get()
    display_label.config(text=text)

root = tk.Tk()
root.title("Text Display")

text_entry = tk.Entry(root)
text_entry.pack(pady=10)

display_button = tk.Button(root, text="Display Text", command=display_text)
display_button.pack(pady=5)

display_label = tk.Label(root, text="")
display_label.pack(pady=10)

root.mainloop()
