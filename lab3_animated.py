import tkinter as tk
from PIL import Image, ImageTk
import random
from pygame import mixer

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WIDTH = 1000
HEIGHT = 700
BG_FILE = "undefined.jpg"
SKY_LEFT   = 0
SKY_TOP    = 0
SKY_RIGHT  = WIDTH
SKY_BOTTOM = int(HEIGHT * 0.3)


def generate_key():
    i = random.randint(0, 25)
    j = random.randint(0, 25)
    a, b = sorted((i, j))
    left = f"{a + 1:02d}"
    right = f"{b + 1:02d}"
    mid = "".join(random.choice(ALPH[a:b + 1]) for _ in range(7))
    return f"{left} {mid} {right}"


def init_frames(root):
    root.title("Terraria Key Generator")
    root.geometry(f"{WIDTH}x{HEIGHT}")

    canvas = tk.Canvas(root, 
                       width=WIDTH, 
                       height=HEIGHT, 
                       highlightthickness=0)
    canvas.pack(fill=tk.BOTH, 
                expand=True)

    img = Image.open(BG_FILE).resize((WIDTH, HEIGHT))
    bg = ImageTk.PhotoImage(img)
    canvas.bg = bg
    canvas.create_image(0, 0, 
                        image=bg, 
                        anchor="nw")

    panel = tk.Frame(root, bg = "#2f4f4f")
    canvas.create_window(WIDTH // 2, 40, 
                         window=panel, 
                         anchor="n")

    title = tk.Label(panel, text="KeyGen",
                     font=("Arial", 16), 
                     bg="#2f4f4f", 
                     fg="white")
    title.pack(pady=8)

    return canvas, panel


def init_controls(panel, canvas, root):
    entry = tk.Entry(panel, 
                     width=32, 
                     font=("Arial", 16))
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

    stars(canvas, root)
    return entry


def stars(canvas, root):
    STAR_SIZE = 3
    FLASH_TIME = 1000
    BATCH = 12
    PERIOD = 200
    MARGIN = 2


    def rand_in_sky():
        x = random.randint(SKY_LEFT + MARGIN,  SKY_RIGHT - MARGIN)
        y = random.randint(SKY_TOP  + MARGIN,  SKY_BOTTOM - MARGIN)
        return x, y


    def tick():
        idx = []
        for _ in range(BATCH):
            x, y = rand_in_sky()
            star = canvas.create_rectangle(x, y, x + STAR_SIZE, y + STAR_SIZE,
                                          fill="white", 
                                          outline="")
            idx.append(star)


        def clear_BATCH():
            for star in idx:
                canvas.delete(star)

        root.after(FLASH_TIME, clear_BATCH)
        root.after(PERIOD, tick)

    tick()


def init_gui():
    root = tk.Tk()
    canvas, panel = init_frames(root)
    init_controls(panel, canvas, root)
    return root


mixer.init()
mixer.music.load("music.wav")
mixer.music.play(-1)


if __name__ == "__main__":
    root = init_gui()
    root.mainloop()
