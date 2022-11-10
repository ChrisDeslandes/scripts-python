from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Nova Janela")
    newWindow.geometry("300x200")
    Label(newWindow, text = "Janela Secundária").pack(pady = 10)
    btnNewWindow = Button(newWindow, text = "Mostrar Mensagem", command = msg)
    btnNewWindow.pack(pady = 10)

def msg():
    messagebox.showinfo(title="?", message="Oi, deu certo?")

master = Tk()
master.title("Novas Janelas")
master.geometry("300x200")

label = Label(master, text = "Janela Principal")
label.pack(pady = 10)

btn = Button(master, text = "Criar Nova Janela", command = openNewWindow)
btn.pack(pady = 10)

master.mainloop()