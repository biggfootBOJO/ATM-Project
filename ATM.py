from tkinter import *

root = Tk()
blank_space = " "
root.title(110 * blank_space + "ATM System")
root.geometry("800x760+280+0")
root.configure(background="gainsboro")
# ============================================frames=====================================================================
Mainframe = Frame(root, bd=20, width=784, height=700, relief=RIDGE)
Mainframe.grid()

Topframe1 = Frame(Mainframe, bd=7, width=734, height=300, relief=RIDGE)
Topframe1.grid(row=1, column=0, padx=12)
Topframe2 = Frame(Mainframe, bd=7, width=734, height=300, relief=RIDGE)
Topframe2.grid(row=0, column=0, padx=8)

Topframe2L = Frame(Topframe2, bd=5, width=190, height=300, relief=RIDGE)
Topframe2L.grid(row=0, column=0, padx=3)

Topframe2M = Frame(Topframe2, bd=5, width=200, height=300, relief=RIDGE)
Topframe2M.grid(row=0, column=1, padx=3)

Topframe2R = Frame(Topframe2, bd=5, width=190, height=300, relief=RIDGE)
Topframe2R.grid(row=0, column=2, padx=3)


# ============================================functions==================================================================
def enter():
    pin_num = root.txtScreen.get("1.0", "end")
    if (pin_num == str("1234")):
        root.txtScreen.delete("1.0", "end")
        root.txtScreen.insert("ATM")

    else:
        root.txtScreen.delete("1.0", "end")
        root.txtScreen.insert(END, 'Invalid Pin')


def num1():
    val1 = str("1")
    root.txtScreen.insert("end", val1)


def num2():
    val2 = str("2")
    root.txtScreen.insert("end", val2)


def num3():
    val3 = str("3")
    root.txtScreen.insert("end", val3)


def num4():
    val4 = str("4")
    root.txtScreen.insert("end", val4)


def num5():
    val5 = str("5")
    root.txtScreen.insert("end", val5)


def num6():
    val6 = str("6")
    root.txtScreen.insert("end", val6)


def num7():
    val7 = str("7")
    root.txtScreen.insert("end", val7)


def num8():
    val8 = str("8")
    root.txtScreen.insert("end", val8)


def num9():
    val9 = str("9")
    root.txtScreen.insert("end", val9)


def num0():
    val0 = str("0")
    root.txtScreen.insert("end", val0)


def clear():
    root.txtScreen.delete("1.0", "end")


# ===========================================images======================================================================
imgArrowL = PhotoImage(file="LArrow.png")
imgArrowR = PhotoImage(file="RArrow.png")

btn1p = PhotoImage(file="one.png")
btn2p = PhotoImage(file="two.png")
btn3p = PhotoImage(file="three.png")
btn4p = PhotoImage(file="four.png")
btn5p = PhotoImage(file="five.png")
btn6p = PhotoImage(file="six.png")
btn7p = PhotoImage(file="seven.png")
btn8p = PhotoImage(file="eight.png")
btn9p = PhotoImage(file="nine.png")
btn0p = PhotoImage(file="zero.png")

imgCE = PhotoImage(file="cancel.png")
imgCL = PhotoImage(file="clear.png")
imgEN = PhotoImage(file="enter.png")
imgSP = PhotoImage(file="empty.png")
# ===========================================widgets====================================================================
root.txtScreen = Text(Topframe2M, height=17, width=42, bd=12, font=("arial", 9, "bold"))
root.txtScreen.grid(row=0, column=0)

btnArrowL1 = Button(Topframe2L, width=160, height=60, image=imgArrowL).grid(row=0, column=0, padx=2, pady=2)
btnArrowL2 = Button(Topframe2L, width=160, height=60, image=imgArrowL).grid(row=1, column=0, padx=2, pady=2)
btnArrowL3 = Button(Topframe2L, width=160, height=60, image=imgArrowL).grid(row=2, column=0, padx=2, pady=2)
# ======================================================================================================================
btnArrowR1 = Button(Topframe2R, width=160, height=60, image=imgArrowR).grid(row=0, column=0, padx=2, pady=2)
btnArrowR2 = Button(Topframe2R, width=160, height=60, image=imgArrowR).grid(row=1, column=0, padx=2, pady=2)
btnArrowR3 = Button(Topframe2R, width=160, height=60, image=imgArrowR).grid(row=2, column=0, padx=2, pady=2)
# ==============================================pin numbers=============================================================
btn1 = Button(Topframe1, width=160, height=60, command=num1, image=btn1p).grid(row=2, column=0, padx=6, pady=4)
btn2 = Button(Topframe1, width=160, height=60, command=num2, image=btn2p).grid(row=2, column=1, padx=6, pady=4)
btn3 = Button(Topframe1, width=160, height=60, command=num3, image=btn3p).grid(row=2, column=2, padx=6, pady=4)
btn4 = Button(Topframe1, width=160, height=60, command=num4, image=btn4p).grid(row=3, column=0, padx=6, pady=4)
btn5 = Button(Topframe1, width=160, height=60, command=num5, image=btn5p).grid(row=3, column=1, padx=6, pady=4)
btn6 = Button(Topframe1, width=160, height=60, command=num6, image=btn6p).grid(row=3, column=2, padx=6, pady=4)
btn7 = Button(Topframe1, width=160, height=60, command=num7, image=btn7p).grid(row=4, column=0, padx=6, pady=4)
btn8 = Button(Topframe1, width=160, height=60, command=num8, image=btn8p).grid(row=4, column=1, padx=6, pady=4)
btn9 = Button(Topframe1, width=160, height=60, command=num9, image=btn9p).grid(row=4, column=2, padx=6, pady=4)
btn0 = Button(Topframe1, width=160, height=60, command=num0, image=btn0p).grid(row=5, column=1, padx=6, pady=4)

btnCE = Button(Topframe1, width=160, height=60, image=imgCE).grid(row=2, column=3, padx=6, pady=4)
btnCL = Button(Topframe1, width=160, height=60, command=clear, image=imgCL).grid(row=3, column=3, padx=6, pady=4)
btnEN = Button(Topframe1, width=160, height=60, command=enter, image=imgEN).grid(row=4, column=3, padx=6, pady=4)

btnEM1 = Button(Topframe1, width=160, height=60, image=imgSP).grid(row=5, column=0, padx=6, pady=4)
btnEM2 = Button(Topframe1, width=160, height=60, image=imgSP).grid(row=5, column=2, padx=6, pady=4)
btnEM3 = Button(Topframe1, width=160, height=60, image=imgSP).grid(row=5, column=3, padx=6, pady=4)

root.mainloop()
