import tkinter as tk

class ToggleButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toggle Button Example")

        self.label = tk.Label(self, text="Toggle the button to change my background color")
        self.label.pack(pady=10)

        self.toggle_var = tk.BooleanVar()
        self.toggle_var.set(False)  # Initial state is False

        self.toggle_button = tk.Checkbutton(self, text="Toggle", variable=self.toggle_var, command=self.toggle_action)
        self.toggle_button.pack()

    def toggle_action(self):
        if self.toggle_var.get():
            self.label.configure(bg="lightblue")  # Change background color when toggle button is checked
        else:
            self.label.configure(bg=self.cget("bg"))  # Reset background color when toggle button is unchecked

if __name__ == "__main__":
    app = ToggleButtonApp()
    app.mainloop()
