import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("Hello World App")

label = tk.Label(root, text="")
label.pack(pady=20)

hello_button = tk.Button(root, text="Press Me", command=say_hello)
hello_button.pack(pady=20)

root.mainloop()
