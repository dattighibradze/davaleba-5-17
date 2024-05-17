import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resize_image(size):
    new_size = int(size)
    resized_image = original_image.resize((new_size, new_size), Image.ANTIALIAS)
    img_label.config(image=ImageTk.PhotoImage(resized_image))

root = tk.Tk()
root.title("Image Resizer")

original_image = Image.open("")
img_label = tk.Label(root)
img_label.pack()

ttk.Scale(root, from_=50, to=500, length=300, orient="horizontal", command=resize_image).pack(pady=10)

resize_image(200)

root.mainloop()
