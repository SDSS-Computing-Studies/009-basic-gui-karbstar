
import tkinter as tk 
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.title("T-Town clinic database")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
button1 = tk.Button(window,text="search by name")
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
label2 = tk.Label(window,text="search by name")
blank = tk.Label(window,text="                                                                                                           ")
label1.grid(row = 0, column = 1)
button1.grid(row = 0, column = 3, sticky=NW )
blank.grid(row = 0, column = 2)
window.mainloop()