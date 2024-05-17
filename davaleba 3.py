import tkinter as tk

def show_window(window):
    window.deiconify()
    root.withdraw()

def back_to_menu(window):
    window.withdraw()
    root.deiconify()

def create_window(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry("300x200")

    tk.Label(window, text=f" {title}!").pack(pady=20)
    tk.Button(window, text="უკან დაბრუნება", command=lambda: back_to_menu(window)).pack()

    return window

root = tk.Tk()
root.title("მენიუ")

menu_label = tk.Label(root, text="მენიუ")
menu_label.pack(pady=20)

button1 = tk.Button(root, text="ფანჯარა 1", command=lambda: show_window(create_window("ფანჯარა 1")))
button1.pack()

button2 = tk.Button(root, text="ფანჯარა 2", command=lambda: show_window(create_window("ფანჯარა 2")))
button2.pack()

button3 = tk.Button(root, text="ფანჯარა 3", command=lambda: show_window(create_window("ფანჯარა 3")))
button3.pack()

root.mainloop()
