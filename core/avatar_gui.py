import tkinter as tk
import math
import threading


class AvatarGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JARVIS AI SYSTEM")
        self.root.geometry("700x700")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(self.root, width=700, height=500, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.angle = 0

        self.status_label = tk.Label(
            self.root,
            text="SYSTEM INITIALIZING",
            fg="#00f0ff",
            bg="black",
            font=("Consolas", 16)
        )
        self.status_label.pack(pady=5)

        self.chat_box = tk.Text(
            self.root,
            height=8,
            bg="black",
            fg="#00f0ff",
            insertbackground="#00f0ff",
            font=("Consolas", 11)
        )
        self.chat_box.pack()

        self.animate()

    def animate(self):
        self.canvas.delete("all")

        center_x = 350
        center_y = 250
        radius = 120

        for i in range(0, 360, 30):
            angle_rad = math.radians(i + self.angle)
            x = center_x + radius * math.cos(angle_rad)
            y = center_y + radius * math.sin(angle_rad)

            self.canvas.create_line(center_x, center_y, x, y, fill="#00f0ff")

        self.canvas.create_oval(
            center_x - 80,
            center_y - 80,
            center_x + 80,
            center_y + 80,
            outline="#00f0ff",
            width=3
        )

        self.angle += 2
        self.root.after(50, self.animate)

    def update_status(self, text):
        self.status_label.config(text=text)

    def add_message(self, sender, message):
        self.chat_box.insert(tk.END, f"{sender}: {message}\n")
        self.chat_box.see(tk.END)

    def run(self):
        self.root.mainloop()