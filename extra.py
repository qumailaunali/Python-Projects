import tkinter as tk
from tkinter import ttk 
root= tk.Tk()
root.geometry("500x300")
text = tk.Label(root,text="hello")
text.grid(row=0,column=0)
combo= ttk.Combobox(root)
combo['values'] = (1,2,4,5)
combo.grid(row=1,column=9)
root.mainloop()