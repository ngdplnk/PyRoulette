import tkinter as tk
import random
import time

def add_name():
    new_name = entry.get()
    if new_name:  # Check if the entry is not empty
        listbox.insert(tk.END, new_name)
        entry.delete(0, tk.END)  # Clear the entry field after adding the name

def spin_roulette():
    if listbox.size() > 0:
        spins = random.randint(10, 20)  # Number of spins before stopping
        delay = 0.1  # Duration between each spin

        for _ in range(spins):
            selected_index = random.randint(0, listbox.size() - 1)
            selected_item = listbox.get(selected_index)
            result_label.config(text=f"Spinning... {selected_item}")
            root.update()  # Update the GUI to show the spinning effect
            time.sleep(delay)

        selected_index = random.randint(0, listbox.size() - 1)
        selected_item = listbox.get(selected_index)
        result_label.config(text=f"Result: {selected_item}")
    else:
        result_label.config(text="Add elements to the roulette first!")

root = tk.Tk()
root.title("Roulette")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter an element:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add", command=add_name)
add_button.grid(row=0, column=2, padx=5, pady=5)

spin_button = tk.Button(frame, text="Spin", command=spin_roulette)
spin_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="we")
 
saved_label = tk.Label(root, text="Added Elements")
saved_label.pack(padx=10, pady=3)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(padx=10, pady=5)

root.mainloop()
