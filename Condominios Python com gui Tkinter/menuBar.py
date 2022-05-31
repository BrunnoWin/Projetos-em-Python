import tkinter as tk
import os
from reuniao_view2 import ReuniaoView
from condominio_view2 import CondominioView
from conexao import Conexao

class MenuBar:
    def __init__(self, window):
        self.window = window

        menuBar = tk.Menu(window)

        cadastroMenu = tk.Menu(menuBar, tearoff = False)
        cadastroMenu.add_command(label = "Consulta/Cadastro de Reunião", command=self._open_reuniao)
        cadastroMenu.add_command(label = "Controle Condominio", command=self._open_condominio)
        cadastroMenu.add_command(label = "Sair", command=window.destroy)
        menuBar.add_cascade(menu = cadastroMenu, label = "Cadastros")

        

        
        window.config(menu=menuBar)

    def _open_reuniao(self):
        janela=tk.Toplevel(self.window)
        principal=ReuniaoView(janela)
        janela.title('Cadastro de Reuniao')
        janela.iconbitmap("imagens\icon.ico")
        janela.geometry("540x500+0+0")
        janela.mainloop()

    def _open_condominio(self):
        janela = tk.Tk()
        principal = CondominioView(janela)
        janela.title("Controle de Condominio")
        janela.iconbitmap("imagens\icon.ico")
        #janela.configure(background='black')
        janela.geometry("590x500+0+0")
        janela.mainloop()

