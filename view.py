import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("500x400")
root.title('Sudoku')
root.resizable(0, 0)

# login button
login_button = ttk.Button(root, text="0")
login_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)


root.mainloop()
