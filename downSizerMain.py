import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((1080, 1350), Image.ANTIALIAS)

        # Find desktop path and save the resized image there
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_path = os.path.join(desktop_path, "resized_image.jpg")
        img.save(output_path)

        img_thumbnail = img.copy()
        img_thumbnail.thumbnail((300, 375))
        img_tk = ImageTk.PhotoImage(img_thumbnail)

        img_label.config(image=img_tk)
        img_label.image = img_tk
        img_label.pack(side="bottom", padx=5, pady=5)


app = tk.Tk()
app.title("Image Resizer")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

open_button = tk.Button(frame, text="Open Image", command=open_image)
open_button.pack(side="top", padx=5, pady=5)

img_label = tk.Label(frame)
img_label.pack(side="bottom", padx=5, pady=5)

app.mainloop()
