import tkinter as tk
import random

def generate_bars(canvas, slider, bars):
    clear_canvas(canvas, bars)
    bar_count = slider.get()

    bar_width = canvas.winfo_reqwidth() / bar_count

    for i in range(bar_count):
        bar_height = random.randint(20, canvas.winfo_reqheight() - 20)
        x_start = i * bar_width
        y_start = canvas.winfo_reqheight()
        bars.append(canvas.create_rectangle(x_start, y_start, x_start + bar_width, y_start - bar_height, fill="#383c8f"))

def rearrangement_bars(canvas, bars):
    bars.sort(key=lambda bar: canvas.coords(bar)[1])
    for i, bar in enumerate(bars):
        x_start = i * (canvas.winfo_reqwidth() / len(bars))
        canvas.coords(bar, x_start, canvas.coords(bar)[1], x_start + (canvas.winfo_reqwidth() / len(bars)), canvas.coords(bar)[3])

def clear_canvas(canvas, bars):
    for bar in bars:
        canvas.delete(bar)
    bars.clear()

screen = tk.Tk()
screen.title("Rearrangement Algorithm")
screen.config(bg="#e69cb1")

canvas_width = 500
canvas_height = 200

canvas = tk.Canvas(screen, width=canvas_width, height=canvas_height, bg="#faf6f5")
canvas.pack(padx=5, pady=(5,0))

slider_label = tk.Label(screen, text="Select a value:", bg="#e69cb1")
slider_label.pack()

slider = tk.Scale(screen, from_=20, to=250, orient=tk.HORIZONTAL, bg="#e69cb1", activebackground="#e391a3")
slider.pack()

start_button = tk.Button(screen, text="Start", command=lambda: generate_bars(canvas, slider, bars), bg="#2dad50", activebackground="#33bd59")
start_button.pack(pady=(5))

rearrangement_button = tk.Button(screen, text="Rearrangement", command=lambda: rearrangement_bars(canvas, bars), bg="#2c97b8", activebackground="#32aacf")
rearrangement_button.pack(pady=(0, 10))

bars = []

screen.mainloop()