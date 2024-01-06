import tkinter as tk
import webbrowser
import random
import time

def add_name():
    new_name = entry.get()
    if new_name:  # Check if the entry is not empty
        listbox.insert(tk.END, new_name)
        entry.delete(0, tk.END)  # Clear the entry field after adding the name

def spin_roulette():
    if listbox.size() > 0:
        spins = random.randint(30, 50)  # Number of spins before stopping
        delay = 0.07  # Duration between each spin

        for _ in range(spins):
            selected_index = random.randint(0, listbox.size() - 1)
            selected_item = listbox.get(selected_index)
            result_label.config(text=f"Girando... {selected_item}", fg="white")
            root.update()  # Update the GUI to show the spinning effect
            time.sleep(delay)

        selected_index = random.randint(0, listbox.size() - 1)
        selected_item = listbox.get(selected_index)
        result_label.config(text=f"Resultado: {selected_item}", fg="green")
    else:
        result_label.config(text="Añade elementos a la ruleta primero!", fg="red")

def open_link(event):
    webbrowser.open("https://www.github.com/ngdplnk/pyroulette")

def callback(event):
    open_link(event)

root = tk.Tk()
root.title("PyRoulette")
root.config(bg="#2b2b2b")
root.minsize(380, 430)

try:
    root.iconbitmap("icon.ico")  # Icon
except tk.TclError:
    print("Error loading icon, running without icon")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
frame.config(bg="#2b2b2b")

title_label = tk.Label(frame, text="PyRoulette", font=("arial", 14, "bold"), bg="#2b2b2b", fg="white")
title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

label = tk.Label(frame, text="Ingresa un elemento:", bg="#2b2b2b", fg="white")
label.grid(row=1, column=0, padx=5, pady=5)

entry = tk.Entry(frame)
entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Añadir", command=add_name)
add_button.grid(row=1, column=2, padx=5, pady=5)

spin_button = tk.Button(frame, text="Girar", command=spin_roulette)
spin_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="we")
 
saved_label = tk.Label(root, text="Elementos añadidos", font=("arial", 10, "bold"), bg="#2b2b2b", fg="white")
saved_label.pack(padx=10, pady=3)

listbox = tk.Listbox(root, width=40, height=10, bg="#2b2b2b", fg="white")
listbox.pack(padx=10, pady=10)

result_label = tk.Label(root, text="Resultado: ", font=("arial", 10, "bold"), bg="#2b2b2b", fg="green")
result_label.pack(padx=10, pady=5)

credits_label = tk.Label(root, text="www.github.com/ngdplnk/pyroulette", font=("arial", 8), bg="#2b2b2b", fg="white", cursor="hand2")
credits_label.pack(padx=10, pady=5)
credits_label.bind("<Button-1>", callback)

root.mainloop()
