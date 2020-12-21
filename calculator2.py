import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("QUMAIL")

screenframe = Frame(root)
screenframe.pack(expand = True,fill = BOTH)

btnframe1 = Frame(root)
btnframe1.pack(expand= True,fill = BOTH)

btnframe2 = Frame(root)
btnframe2.pack(expand= True,fill = BOTH)

btnframe3 = Frame(root)
btnframe3.pack(expand= True,fill = BOTH)

btnframe4 = Frame(root)
btnframe4.pack(expand= True,fill = BOTH)


val = ""
operator = ""
def btn_1_click():
    global val
    val = val + "1"
    data.set(val)

def btn_2_click():
    global val
    val = val + "2"
    data.set(val)

def btn_3_click():
    global val
    val = val + "3"
    data.set(val)

def btn_4_click():
    global val
    val = val + "4"
    data.set(val)

def btn_5_click():
    global val
    val = val + "5"
    data.set(val)

def btn_6_click():
    global val
    val = val + "6"
    data.set(val)

def btn_7_click():
    global val
    val = val + "7"
    data.set(val)

def btn_8_click():
    global val
    val = val + "8"
    data.set(val)


def btn_9_click():
    global val
    val = val + "9"
    data.set(val)

def btn_0_click():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_click():
    global val
    global operator

    val = val + "+"
    operator = "+"
    data.set(val)

def btn_minus_click():
    global val
    global operator

    val = val + "-"
    operator = "-"
    data.set(val)

def btn_mul_click():
    global val
    global operator

    val = val + "*"
    operator = "*"
    data.set(val)

def btn_div_click():
    global val
    global operator
    val = val + "/"
    operator = "/"
    data.set(val)


def btn_equal_click():
    global val
    global operator
    # split val
    val1 = val
    x = val1.split(operator)
    if operator == "+":
        result = int(x[0]) + int(x[1])
        val = result
        val = str(val)        

    elif operator == "-":
        result = int(x[0]) - int(x[1])
        val = result
        val = str(val)        

    elif operator == "*":
        result = int(x[0]) * int(x[1])
        val = result
        val = str(val)        

    elif operator == "/":
        result = int(x[0])/int(x[1])
        val = result
        val = str(val)        
    data.set(val)












def btn_clear_click():
    global val
    val = ""
    data.set(val)




data = StringVar()





label1 = Label(
    screenframe,
    font = ("vaardana", 22),
    anchor = SE,    
    textvariable = data,
)
label1.pack(expand= True,fill = BOTH)


btn1= Button(
    btnframe1,
    text = "1",
    font = ("vardana", 22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_1_click

)
btn1.pack(expand= True,fill = BOTH,side= LEFT)

btn2= Button(
    btnframe1,
    text = "2",
    font = ("vardana", 22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_2_click

)
btn2.pack(expand= True,fill = BOTH,side= LEFT)

btn3= Button(
    btnframe1,
    text = "3",
    font = ("vardana", 22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_3_click

)
btn3.pack(expand= True,fill = BOTH,side= LEFT)

btnplus= Button(
    btnframe1,
    text = "+",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_plus_click

)
btnplus.pack(expand= True,fill = BOTH,side= LEFT)

btn4= Button(
    btnframe2,
    text = "4",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_4_click

)
btn4.pack(expand= True,fill = BOTH,side= LEFT)

btn5= Button(
    btnframe2,
    text = "5",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_5_click

)
btn5.pack(expand= True,fill = BOTH,side= LEFT)

btn6= Button(
    btnframe2,
    text = "6",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_6_click

)
btn6.pack(expand= True,fill = BOTH,side= LEFT)

btnminus= Button(
    btnframe2,
    text = "-",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_minus_click

)
btnminus.pack(expand= True,fill = BOTH,side= LEFT)

btn7= Button(
    btnframe3,
    text = "7",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_7_click

)
btn7.pack(expand= True,fill = BOTH,side= LEFT)

btn8= Button(
    btnframe3,
    text = "8",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_8_click

)
btn8.pack(expand= True,fill = BOTH,side= LEFT)

btn9= Button(
    btnframe3,
    text = "9",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_9_click

)
btn9.pack(expand= True,fill = BOTH,side= LEFT)

btnmul= Button(
    btnframe3,
    text = "*",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_mul_click

)
btnmul.pack(expand= True,fill = BOTH,side= LEFT)

btnclear= Button(
    btnframe4,
    text = "C",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_clear_click

)
btnclear.pack(expand= True,fill = BOTH,side= LEFT)

btn0= Button(
    btnframe4,
    text = "0",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_0_click

)
btn0.pack(expand= True,fill = BOTH,side= LEFT)

btnequal= Button(
    btnframe4,
    text = "=",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_equal_click

)
btnequal.pack(expand= True,fill = BOTH,side= LEFT)

btndiv= Button(
    btnframe4,
    text = "/",
    font = ("vardana",22),
    borderwidth=0,
    relief = GROOVE,
    command = btn_div_click

)
btndiv.pack(expand= True,fill = BOTH,side= LEFT)












root.mainloop()