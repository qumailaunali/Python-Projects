import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import  os

application = tk.Tk()
application.geometry('1200x800')
application.title("QPAD")

# # ----------------------------------------------------------------Main menu------------------------------------------
# main_menu = tk.Menu()
# # file_icons
# new_icon = tk.PhotoImage(file='icons/new.png')
# open_icon = tk.PhotoImage(file='icons/open.png')
# save_icon = tk.PhotoImage(file='icons/save.png')
# save_as_icon = tk.PhotoImage(file='icons/save_as.png')
# exit_icon = tk.PhotoImage(file='icons/exit.png')


# file = tk.Menu(main_menu, tearoff = False)

# file.add_command(label='new',image=new_icon, compound=tk.LEFT,accelerator='Ctrl+N')
# file.add_command(label='Open',image=open_icon, compound=tk.LEFT,accelerator='Ctrl+O')
# file.add_command(label='Save',image=save_icon, compound=tk.LEFT,accelerator='Ctrl+S')
# file.add_command(label='Save As',image=save_as_icon, compound=tk.LEFT,accelerator='Ctrl+Alt+S')
# file.add_command(label='Exit',image=exit_icon, compound=tk.LEFT,accelerator='Ctrl+Q')

# # edit icons
# copy_icon = tk.PhotoImage(file='icons/copy.png')
# paste_icon = tk.PhotoImage(file='icons/paste.png')
# cut_icon = tk.PhotoImage(file='icons/cut.png')
# clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
# find_icon = tk.PhotoImage(file='icons/find.png')

# edit = tk.Menu(main_menu, tearoff = False)
# edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,command =None,accelerator='CTRL+C')
# edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,command =None,accelerator='CTRL+V')
# edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,command =None,accelerator='CTRL+X')
# edit.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,command =None,accelerator='CTRL+ALT+C')
# edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,command =None,accelerator='CTRL+F')
# # view menu
# tool_bar_icon = tk.PhotoImage(file=r"C:\Users\sonof\Desktop\icons\tool_bar.png")
# status_bar_icon = tk.PhotoImage(file=r"C:\Users\sonof\Desktop\icons\status_bar.png")
 
# view = tk.Menu(main_menu, tearoff = False)


# color_theme = tk.Menu(main_menu, tearoff = False)

# main_menu.add_cascade(label='File', menu= file)
# main_menu.add_cascade(label='Edit', menu= edit)
# main_menu.add_cascade(label='View', menu= view)
# main_menu.add_cascade(label='Color Theme', menu= color_theme)



# # ----------------------------------------------------------------Tool bar-------------------------------------------


# # ----------------------------------------------------------------Text editor----------------------------------------


# # ----------------------------------------------------------------Main statsu bar------------------------------------


# # ---------------------------------------------------------------Main menu funtionality-----------------------------
# application.config(menu=main_menu)
application.mainloop()