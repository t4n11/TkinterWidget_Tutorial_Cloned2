import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('Tkinter Spinbox Widget)')
window.geometry('400x400')
int_var = tk.IntVar()
Number_spinbox = ttk.Spinbox(window, from_=0, to=100, increment= .01, textvariable = int_var, font = 'Calibri 24 bold')
Number_spinbox.pack()
window.mainloop()