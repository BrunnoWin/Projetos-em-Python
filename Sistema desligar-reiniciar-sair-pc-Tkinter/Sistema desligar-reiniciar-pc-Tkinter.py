from tkinter import *
import os


def desligar():
    return os.system("shutdown /s /t 1")


def reiniciar():
    return os.system("shutdown /r /t 1")


def sair():
    return os.system("shutdown -l")

janela = Tk()
janela.geometry("120x130")
janela.configure(bg='light grey')
Button(janela, text='Desligar', command=desligar).place(x=20,y=20)
Button(janela, text='Reiniciar', command=reiniciar).place(x=19,y=50)
Button(janela, text='Sair', command=sair).place(x=32,y=80)

janela.mainloop()