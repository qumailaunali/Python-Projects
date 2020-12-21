import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()
win.geometry("500x400")
win.title('GUI')

def func():
    None
# --------------------menu-------
menu_bar = tk.Menu(win)

file_menu = tk.Menu(menu_bar,tearoff = 0)
file_menu.add_command(label = 'New File',command= func)
file_menu.add_separator()
file_menu.add_command(label = 'Save',command= func)
file_menu.add_command(label = 'Save As',command= func)

help_menu = tk.Menu(menu_bar,tearoff = 0)
help_menu.add_command(label = 'About',command = func)
help_menu.add_separator()
help_menu.add_command(label = 'GO',command = func)

menu_bar.add_cascade(label = 'Files',menu=file_menu )
menu_bar.add_cascade(label = 'Help',menu=help_menu )

win.config(menu = menu_bar)
# ---------------
# -------------------------- notebook
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1,text='One')
nb.add(page2,text='Two')

nb.pack(expand = True,fill = 'both')

labelwin = ttk.LabelFrame(page1, text = 'USER DETAILS')
labelwin.grid(row=0,column=0,padx=100,pady=70)

#---------------------label
lis = ['Name : ', 'Age :','Field: ']
for x,y in enumerate(lis):
    label = ttk.Label(labelwin, text =y,font = ('Museo Sans Rounded 100',14)) 
    label.grid(row=x,column = 0,sticky=tk.W)



user_info = { 
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'field': tk.StringVar()
}

entrybox1 = ttk.Entry(labelwin,width=16, textvariable = user_info['name'])
entrybox1.grid(row=0,column=1)

entrybox2 = ttk.Entry(labelwin,width=16, textvariable = user_info['age'])
entrybox2.grid(row=1,column=1)
    
entrybox3 = ttk.Radiobutton(labelwin,text = 'Male',value = 'Male', variable = user_info['field'])
entrybox3.grid(row=2,column=1)
entrybox3 = ttk.Radiobutton(labelwin,text = 'Female',value = 'Female', variable = user_info['field'])
entrybox3.grid(row=2,column=2,)

# name_var = tk.StringVar()
# name_entry = ttk.Entry(labe)

for child in labelwin.winfo_children():
    child.grid_configure(padx=10,pady=10)

def action():
    name = user_info['name'].get()
    age = user_info['age'].get()
    if name == '' or age == '':
        m_box.showerror('Error', 'Please fill all the fields')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('Error','Only digits allow in age field')
        else:
            with open(r'\users\sonof\Desktop\info.txt','a') as f:
                a,b,c = (user_info['name'].get(),user_info['age'].get(),user_info['field'].get())
                f.write(f'User name is {a}, age {b} and gender {c}\n')
    
            entrybox1.delete(0,tk.END)
            entrybox2.delete(0,tk.END)
            m_box.showinfo('Done!','Your information is saved')
        
sub = ttk.Button(labelwin,width=16,text='Submit',command= action)
sub.grid(row=4,columnspan=2)
win.mainloop()