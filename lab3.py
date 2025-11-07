import tkinter as tk
from PIL import Image, ImageTk
import random
from string import ascii_uppercase

ALPH = ascii_uppercase
WIDTH = 1000
HEIGHT = 700


def generate_key():
    i = random.randint(0, 25)
    j = random.randint(0, 25)
    i, j = sorted((i, j))
    left  = f"{i + 1:02d}"
    right = f"{j + 1:02d}"
    letters = "".join(random.choice(ALPH[i:j+1]) for _ in range(7))
    return f"{left} {letters} {right}"


def init_frames(root):
    root.title("Terraria Key Generator")
    root.geometry(f'{WIDTH}x{HEIGHT}')

    img = Image.open("undefined.jpg")
    img = img.resize((WIDTH,HEIGHT))
    bg = ImageTk.PhotoImage(img)

    frame_main = tk.Frame(root)
    frame_main.pack(fill=tk.BOTH, expand=True)

    bg_label = tk.Label(frame_main, image=bg)
    bg_label.image = bg
    bg_label.place(x=0,
                   y=0,
                   relwidth=1,
                   relheight=1,)


    panel = tk.Frame(frame_main, bg="#2f4f4f")
    panel.pack(pady=30)
    title = tk.Label(panel,
                     text="KeyGen",
                     font=("Arial", 16),
                      bg="#2f4f4f", 
                      fg="white")
    title.pack(pady=8)

    return panel


def init_controls(panel):
    entry = tk.Entry(panel,
                     width=32,
                     font=("Arial", 14))
    entry.pack(side=tk.LEFT,
               padx=6,
               pady=6)


    def generate():
        key = generate_key()
        entry.delete(0, tk.END)
        entry.insert(0, key)

    btn = tk.Button(panel,
                    text="Сгенерировать ключ",
                    command=generate)
    btn.pack(side=tk.LEFT,
                padx=6)

    return entry


def init_gui():
    root = tk.Tk()
    panel = init_frames(root)
    init_controls(panel)
    return root


if __name__ == "__main__":
    root = init_gui()
    root.mainloop()

