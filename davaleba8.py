import tkinter as tk

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Game Prototype")
        self.geometry("400x400")

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        self.character = self.canvas.create_rectangle(180, 180, 220, 220, fill="blue")  # Character rectangle

        # Button to move character up
        self.btn_up = tk.Button(self, text="Up", command=self.move_up)
        self.btn_up.pack(side=tk.TOP, pady=5)

        # Button to move character down
        self.btn_down = tk.Button(self, text="Down", command=self.move_down)
        self.btn_down.pack(side=tk.BOTTOM, pady=5)

        # Button to move character left
        self.btn_left = tk.Button(self, text="Left", command=self.move_left)
        self.btn_left.pack(side=tk.LEFT, padx=5)

        # Button to move character right
        self.btn_right = tk.Button(self, text="Right", command=self.move_right)
        self.btn_right.pack(side=tk.RIGHT, padx=5)

    def move_up(self):
        self.canvas.move(self.character, 0, -10)

    def move_down(self):
        self.canvas.move(self.character, 0, 10)

    def move_left(self):
        self.canvas.move(self.character, -10, 0)

    def move_right(self):
        self.canvas.move(self.character, 10, 0)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
