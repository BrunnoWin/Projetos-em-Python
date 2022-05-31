import tkinter as tk
from tkinter import Text, ttk
from tkinter import messagebox as mb
from tkinter.constants import END
from typing import Sized
from conexao import Conexao

#1 - Adicionando botões e posionando na tela.

from condominio import Condominio

class CondominioView:

    def __init__(self, win):
        self.condominioCRUD = Condominio()

        #TELA

        self.cpfLabel = tk.Label(win, text='CPF:')
        self.cpfEdit = tk.Entry(win,width = 30, bd=2)

        self.nomeLabel = tk.Label(win, text='Nome Proprieatrio:')
        self.nomeEdit = tk.Entry(win, width=30, bd=2)
       

        self.apartamentoLabel = tk.Label(win, text='Apartamento:')
        self.apartamentoEdit = tk.Entry(win,width = 30, bd=2)

        self.telefoneLabel = tk.Label(win, text='Telefone:')
        self.telefoneEdit = tk.Entry(win,width = 30, bd=2)




        self.btnCadastrar = tk.Button(win, text='Cadastrar', width=7, command=self._on_cadastrar_clicked)

        self.btnCadastrar.place(x=350,y=175)
        #self.btnConsultar = tk.Button(win, text='Consultar', width=7, command=self._on_consultar_clicked)
        self.btnAlterar = tk.Button(win, text='Alterar', width=7, command=self._on_atualizar_clicked)
        self.btnAlterar.place(x=350,y=115)

        self.btnExcluir = tk.Button(win, text='Excluir', width=7, command=self._on_excluir_clicked)
        self.btnExcluir.place(x=350,y=145)


        self.condominioList = ttk.Treeview(win, columns=(1,2,3,4,5), show='headings')

        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.condominioList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.condominioList.configure(yscrollcommand = self.verscrlbar.set)

        self.condominioList.heading(1, text='ID')
        self.condominioList.heading(2, text='CPF')
        self.condominioList.heading(3, text='Nome Proprieatrio')
        self.condominioList.heading(4, text='Apartamento')
        self.condominioList.heading(5, text='Telefone')

        self.condominioList.column(1, minwidth=0, width=20)
        self.condominioList.column(2, minwidth=0, width=50)
        self.condominioList.column(3, minwidth=0, width=120)
        self.condominioList.column(4, minwidth=0, width=50)
        self.condominioList.column(5, minwidth=0, width=50)


        self.condominioList.pack()
        self.condominioList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)
        
    

        #Posicionar os componentes na tela


        self.cpfLabel.place(x=90,y=50)#texto  x=3,y=50 | x=115,y=80
        self.cpfEdit.place(x=130,y=50)#quadrado  x=60,y=50 | x=150,y=80

        self.nomeLabel.place(x=10,y=80)#texto  x=250,y=50
        self.nomeEdit.place(x=130,y=80)#quadrado  x=300,y=50

        #self.textoLabel.place(x=130,y=5)#texto banner criado CONSULTAR/CADASTRAR REUNIÃO /self.textoLabel.place(x=180,y=30)

        self.apartamentoLabel.place(x=40,y=110)#texto
        self.apartamentoEdit.place(x=130,y=110)#quadrado

        self.telefoneLabel.place(x=70,y=140)#texto
        self.telefoneEdit.place(x=130,y=140)

        #botao de alteraçoes mais compontentes
        #self.btnCadastrar.place(x=350,y=175)

        #self.btnCadastrar = tk.Button(win, 
          #      text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)


        #------------------
        self.condominioList.place(x=40,y=250, height=180,width=490)
        self.verscrlbar.place(x=530,y=250, height=180)
        self.carregar_dados_iniciais_treeView()

    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto

        cpf = self.cpfEdit.get()
        nome = self.nomeEdit.get()
        apartamento = self.apartamentoEdit.get()
        telefone = self.telefoneEdit.get()
        



        if self.condominioCRUD.cadastrar(cpf,nome,apartamento,telefone):
            #Atualizar a TreeView           
           numeroLinhas = len(self.condominioList.get_children())
           id =  self.condominioCRUD.consultar_ultimo_id()
           self.condominioList.insert('','end',iid = numeroLinhas, values=(str(id),cpf,nome,apartamento,telefone))
           mb.showinfo("Mensagem", "Cadastro executado com sucesso.")
            #Limpar os campos texto
           self.cpfEdit.delete(0,tk.END)
           self.nomeEdit.delete(0,tk.END)
           self.apartamentoEdit.delete(0,tk.END)
           self.telefoneEdit.delete(0,tk.END)
         
        else:
            mb.showinfo("Mensagem", "Erro no cadastro.")
            self.cpfEdit.focus_set()
            self.nomeEdit.focus_set()
            self.apartamentoEdit.focus_set()
            self.telefoneEdit.focus_set()

    def _on_mostrar_clicked(self, event):#event e necessario para aparece dados epois que 
        selection = self.condominioList.selection()
        item = self.condominioList.item(selection[0])

        cpf = item["values"][1]
        nome = item["values"][2]
        apartamento = item["values"][3]
        telefone = item["values"][4]
       
        self.cpfEdit.delete(0, tk.END)
        self.cpfEdit.insert(0,cpf)

        self.nomeEdit.delete(0, tk.END)
        self.nomeEdit.insert(0,nome)

        self.apartamentoEdit.delete(0, tk.END)
        self.apartamentoEdit.insert(0,apartamento)

        self.telefoneEdit.delete(0, tk.END)
        self.telefoneEdit.insert(0,telefone)
    

    def _on_atualizar_clicked(self):
        linhaSelecionada = self.condominioList.selection()
      
        if len(linhaSelecionada) != 0:
            id= self.condominioList.item(linhaSelecionada[0])["values"][0]

              
            cpf = self.cpfEdit.get()
    
            nome = self.nomeEdit.get()
        
            apartamento = self.apartamentoEdit.get()
       
            telefone = self.telefoneEdit.get()
         


            if  self.condominioCRUD.atualizar(id,cpf,nome,apartamento,telefone):

                self.condominioList.item(self.condominioList.focus(), values=(str(id),cpf,nome,apartamento,telefone))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.cpfEdit.delete(0, tk.END)
                self.nomeEdit.delete(0, tk.END)
                self.apartamentoEdit.delete(0, tk.END)
                self.telefoneEdit.delete(0, tk.END)
            
               
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")
                self.cpfEdit.focus_set()
                self.nomeEdit.focus_set()
                self.apartamentoEdit.focus_set()
                self.telefoneEdit.focus_set()
    
    def _on_excluir_clicked(self):
        linhaSelecionada = self.condominioList.selection()

        if len(linhaSelecionada) != 0:
            id = self.condominioList.item(linhaSelecionada[0])["values"][0]

            if  self.condominioCRUD.excluir(id):
                self.condominioList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.cpfEdit.delete(0, tk.END)
                self.nomeEdit.delete(0, tk.END)
                self.apartamentoEdit.delete(0, tk.END)
                self.telefoneEdit.delete(0, tk.END)
              
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.cpfEdit.focus_set()
                self.nomeEdit.focus_set()
                self.apartamentoEdit.focus_set()
                self.telefoneEdit.focus_set()
    







    def carregar_dados_iniciais_treeView(self):
        registros = self.condominioCRUD.consultar()

        count = 0
        for item in registros:
            id = item[0]
            cpf = item[1]
            nome = item[2]
            apartamento = item[3]
            telefone = item[4]
          
            self.condominioList.insert('','end',iid=count, values=(str(id),cpf,nome,apartamento,telefone))
            count = count + 1

            


    #2 - Adicionando frases na tela.


#janela = tk.Tk()
#principal = CondominioView(janela)
#janela.title("Controle de Condominio")
#janela.iconbitmap("imagens\icon.ico")
#janela.configure(background='black')
#janela.geometry("590x500+0+0")
#janela.mainloop()




