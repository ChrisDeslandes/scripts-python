from tkinter import *

def btnclick():
    global clicou
    clicou = True
    if selecao.get() == 1:
        try:
            c = float(tempC.get())
            tempF.set(str(round(c*1.8 + 32, 2)))
        except ValueError:
            pass
    else:
        try:
            f = float(tempF.get())
            tempC.set(str(round((f - 32)/1.8, 2)))
        except ValueError:
            pass
    clicou = False

def mudarSelecaoPara1():
    if not clicou: selecao.set(1)

def mudarSelecaoPara2():
    if not clicou: selecao.set(2)

clicou = False

window = Tk()
window.title("Conversor de temperatura")
window.resizable(width=False, height=False)
#window.geometry('%dx%d+%d+%d' % (375, 125, (window.winfo_screenwidth() / 2) - (375 / 2), (window.winfo_screenheight() / 2) - (125 / 2)))
window.geometry('%dx%d+%d+%d' % (375, 125, (window.winfo_screenwidth() - 383), 0))

f1 = Frame(window, width=320, height=20)
f1.pack_propagate(0)
f1.place(x = 10, y = 10)

selecao = IntVar()

tempC = StringVar()
tempC.trace("w", lambda *args: mudarSelecaoPara1())
tempCEntered = Entry(f1, textvariable = tempC)
tempCEntered.pack(fill=BOTH, expand=1)

lbl1 = Label(window, text = "ºC", fg = "red", font = ("Arial", 12))
lbl1.place(x = 335, y = 10)

f2 = Frame(window, width=320, height=20)
f2.pack_propagate(0)
f2.place(x = 10, y = 40)

tempF = StringVar()
tempF.trace("w", lambda *args: mudarSelecaoPara2())
tempFEntered = Entry(f2, textvariable = tempF)
tempFEntered.pack(fill=BOTH, expand=1)

lbl2 = Label(window, text = "ºF", fg = "red", font = ("Arial", 12))
lbl2.place(x = 335, y = 40)

rb1 = Radiobutton(window, text = "ºC para ºF", variable=selecao, value=1)
rb1.place(x = 10, y = 70)
rb2 = Radiobutton(window, text = "ºF para ºC", variable=selecao, value=2)
rb2.place(x = 10, y = 90)
selecao.set(1)

f3 = Frame(window, height=45, width=105)
f3.pack_propagate(0)
f3.place(x = 255, y = 70)

btn = Button(f3, text = "Calcular", command = btnclick, fg = "black", font = ("Arial",10))
btn.pack(fill=BOTH, expand=1)

window.bind('<Return>', (lambda e, b=btn: b.invoke()))

tempCEntered.focus()
window.mainloop()
