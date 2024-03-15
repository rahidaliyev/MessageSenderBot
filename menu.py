import tkinter as tk
from findImage import get_image

def get_input():
    image_text = entry.get()
    get_image(image_text)
window = tk.Tk()
window.title("Menu")

label = tk.Label(window, text="Search_Keyword")
label.pack()

entry = tk.Entry(window, width=30)

button = tk.Button(window, text="Get Input", command=get_input)


window.geometry("400x250")
entry.pack(pady=15)
button.pack(pady=10)

window.mainloop()