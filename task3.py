"""
Create the user interface described in the image task3.png
using the .grid() method
(3 points)
"""
import tkinter as tk 
from tkinter import *
from tkinter import ttk
window = tk.Tk()
mov= tk.Label(window,text="                        ")
window.title("T-Town clinic database")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label1.grid(row = 0, column = 1,)
u3 = tk.Label(window,text="pochacco!           ")
u3.grid(row=0, column = 1, sticky=E )
u = tk.Label(window,text="a cuddly little puppy! This is from the same\ncreators who brought you keropi and kero kero", bg="#00e2ee")
u.grid(row=2, column = 1, )
window.mainloop()