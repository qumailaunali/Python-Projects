import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("1080x620+420+210")
win.resizable(False,False)

combo = ttk.Combobox(win,width= 45)
combo['values']= ("MIlk","Eggs","Bread")
combo.pack(anchor= 'sw', padx= 400, pady = 30 )




win.mainloop()