import tkinter as tk

from tkinter import ttk

# This section creates the Tkinter Window and adds the required elements to it

window = tk.Tk()

window.title('Tkinter Text Entry Widget')

window.geometry('400x400')

def get_button1_text():

    t = 'button1 clicked' 

    output_string.set(t)

def get_button2_text():

    t = 'button2 clicked'

    output_string.set(t)


# button – When pressed runs the function that calculates the Grade "get_grade()"

button_1 = ttk.Button(master = window, text = 'BUTTON 1', command = get_button1_text)

button_2 = ttk.Button(master = window, text = 'BUTTON 2', command = get_button2_text)

# output Label

output_string = tk.StringVar()

output_label = ttk.Label(master = window, textvariable = output_string)

# Pack elements in frames ready to push onto form/window

#Text_entry.pack();

button_1.pack();

button_2.pack();

output_label.pack();

# run the program to generate window with all packed elements for user interaction

window.mainloop()

 
import tkinter as tk

from tkinter import ttk
 
# Create window

window = tk.Tk()

window.title('Tkinter Text Entry Widget')

window.geometry('400x300')
 
# Output label

output_string = tk.StringVar()

output_label = ttk.Label(window, textvariable=output_string)

output_label.pack(pady=10)
 
# Function to confirm which button is pressed

def button1_pressed():

    output_string.set("Option 1 pressed!")
 
def button2_pressed():

    output_string.set("Option 2 pressed!")
 
# LabelFrame with two buttons

choice_frame = ttk.LabelFrame(window, text="My Choice")

choice_frame.pack(pady=20, padx=20, fill="x")
 
button1 = ttk.Button(choice_frame, text="Option 1", command=button1_pressed)

button1.pack(side="left", padx=10, pady=10)
 
button2 = ttk.Button(choice_frame, text="Option 2", command=button2_pressed)

button2.pack(side="left", padx=10, pady=10)
 
# Run

window.mainloop()

 