import tkinter as tk 
from tkinter import *
from tkinter import ttk
window = tk.Tk()
mov= tk.Label(window,text="                        ")
window.title("T-Town clinic database")
window.geometry("254x135")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
u3 = tk.Label(window,text="pochacco!           ")
u = tk.Label(window,text="a cuddly little puppy! This is from the same\ncreators who brought you keropi and kero kero", bg="#00e2ee")
label1.place(x=100,y=0)
u.place(x=0,y=100)
u3.place(x=170,y=35)
window.mainloop()