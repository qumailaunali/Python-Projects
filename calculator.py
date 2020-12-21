import tkinter
from tkinter import *
from tkinter import messagebox
root = tkinter.Tk()
root.geometry("270x400+300+300")
root.resizable(0,0)
root.title(" CALCULATOR")

val = ""
a = 0
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
    global a
    global operator
    a = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_click():
    global val
    global a
    global operator
    a = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_click():
    global val
    global a
    global operator
    a = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_click():
    global val
    global a
    global operator
    a = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_click():
    global val
    global a
    global operator
    val = ""
    a = 0
    operator = ""
    data.set(val)


def result():
    global val
    global a
    global operator
    val2 = val
    x = int((val2.split(operator)[1]))
    if operator == "+":
        rest = a + int(x)
    elif operator == "-":
        rest = a - int(x)
    elif operator == "*":
        rest = a * int(x)
    elif operator == "/":
        if x == 0:
            messagebox.showerror("CAN'T divide with zero")
            a = ""
            val = ""
            operator = ""
            data.set(val)
        else:
            rest = a/int(x)
            data.set(rest)
            val = str(rest)

        rest = a/int(x)

    data.set(rest)
    val = str(rest)

    
data = StringVar()
lbl = Label(
    root,
    text= "Label",
    anchor = SE,
    font = ("Verdana",22),
    textvariable = data,
    fg = "#000000"
)
lbl.pack(expand = True,fill = "both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand = True,fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True,fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True,fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True,fill = "both")



btn1 = Button(
    btnrow1,
    text = "1",
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_1_click,

)
btn1.pack(side = LEFT, expand = True,fill = "both")

btn2 = Button(
    btnrow1, 
    text = "2", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_2_click,
)
btn2.pack(side = LEFT, expand = True,fill = "both")

btn3 = Button(
    btnrow1, 
    text = "3", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_3_click,
)
btn3.pack(side = LEFT, expand = True,fill = "both")

btnplus = Button(
    btnrow1, 
    text = "+", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_click,
)
btnplus.pack(side = LEFT, expand = True,fill = "both")



btn4 = Button(
    btnrow2, 
    text = "4", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_4_click,
)
btn4.pack(side = LEFT, expand = True,fill = "both")

btn5 = Button(
    btnrow2, 
    text = "5", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_5_click,
)
btn5.pack(side = LEFT, expand = True,fill = "both")

btn6 = Button(
    btnrow2, 
    text = "6",
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_6_click,
)
btn6.pack(side = LEFT, expand = True,fill = "both")

btnmin = Button(
    btnrow2, 
    text = "-", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_click,
)
btnmin.pack(side = LEFT, expand = True,fill = "both")

btn7 = Button(
    btnrow3, 
    text = "7", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_7_click,
)
btn7.pack(side = LEFT, expand = True,fill = "both")

btn8 = Button(
    btnrow3, 
    text = "8", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_8_click,
)
btn8.pack(side = LEFT, expand = True,fill = "both")

btn9 = Button(
    btnrow3, 
    text = "9", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_9_click,
)
btn9.pack(side = LEFT, expand = True,fill = "both")

btnmul = Button(
    btnrow3, 
    text = "*", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_mul_click,
)
btnmul.pack(side = LEFT, expand = True,fill = "both")

btnclear = Button(
    btnrow4,
    text = "C", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_c_click,
)
btnclear.pack(side = LEFT, expand = True,fill = "both")

btn0 = Button(
    btnrow4, 
    text = "0", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_0_click,
)
btn0.pack(side = LEFT, expand = True,fill = "both")

btnequal = Button(
    btnrow4, 
    text = "=", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    comman = result,
)
btnequal.pack(side = LEFT,expand = True,fill = "both")

btndiv = Button(
    btnrow4, 
    text = "/", 
    font =("Verdana",22),
    relief = GROOVE,
    border = 0,
    command = btn_div_click,
)
btndiv.pack(side = LEFT, expand = True,fill = "both")



root.mainloop()
