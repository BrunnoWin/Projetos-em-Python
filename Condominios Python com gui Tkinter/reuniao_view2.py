import tkinter as tk
from tkinter import Text, ttk
from tkinter import messagebox as mb
from tkinter.constants import END
from typing import Sized
from conexao import Conexao



from reuniao import Reuniao

class ReuniaoView:

    def __init__(self,win):
        self.reuniaoCRUD = Reuniao()


        

        #Criar os componentes de tela

        self.textoLabel = tk.Label(win, text='CONSULTAR/CADASTRAR\nREUNIÃO', font="impact 20")
        
        self.pesquisaLabel = tk.Label(win, text='Pesquisar ID:')
        self.pesquisaEdit = tk.Entry(win, width = 13, bd=2)
        #self.btnBuscar = tk.Button(win, text='Buscar', command=self._on_buscar_clicked,  y=200)
        self.btnBuscar = tk.Button(win, 
                text = 'Buscar', width = 7, command=self._on_buscar_clicked)

        self.dataLabel = tk.Label(win, text='Data:')
        self.dataEdit = tk.Entry(win, width = 10, bd=2)#win para retirar bug que esta dando no application

        self.horaLabel = tk.Label(win, text='Hora:')
        self.horaEdit = tk.Entry(win,width = 10, bd=2)
        
        
         
        self.assuntoLabel = tk.Label(win, text='Assunto:')
        #self.assuntoEdit = tk.Entry(width = 30, bd=2)

        self.assuntoEdit = tk.Text(win, height=5, width=27)
        #self.assuntoEdit.pack()
        
        self.btnCadastrar = tk.Button(win, 
                text = 'Cadastrar', width = 7, command=self._on_cadastrar_clicked)

        self.btnAlterar = tk.Button(win, 
                text = 'Alterar', width = 7, command=self._on_atualizar_clicked)

        self.btnExcluir = tk.Button(win, 
                text = 'Excluir', width = 7, command=self._on_deletar_clicked)


        self.reuniaoList = ttk.Treeview(win, columns=(1,2,3,4), show='headings')

        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.reuniaoList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.reuniaoList.configure(yscrollcommand = self.verscrlbar.set)

        self.reuniaoList.heading(1, text='ID')
        self.reuniaoList.heading(2, text='Data')
        self.reuniaoList.heading(3, text='Hora')
        self.reuniaoList.heading(4, text='Assunto')

        self.reuniaoList.column(1, minwidth=0, width=50)
        self.reuniaoList.column(2, minwidth=0, width=70)
        self.reuniaoList.column(3, minwidth=0, width=50)
        self.reuniaoList.column(4, minwidth=0, width=250)#4, minwidth=0, width=217



        
       
        self.reuniaoList.pack()
        self.reuniaoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)


        #Posicionar os componentes na tela


        self.dataLabel.place(x=130,y=80)#texto  x=3,y=50 | x=115,y=80
        self.dataEdit.place(x=170,y=80)#quadrado  x=60,y=50 | x=150,y=80

        self.horaLabel.place(x=250,y=80)#texto  x=250,y=50
        self.horaEdit.place(x=300,y=80)#quadrado  x=300,y=50

        self.textoLabel.place(x=130,y=5)#texto banner criado CONSULTAR/CADASTRAR REUNIÃO /self.textoLabel.place(x=180,y=30)

        self.assuntoLabel.place(x=60,y=150)#texto
        self.assuntoEdit.place(x=120,y=120)#quadrado

        self.pesquisaLabel.place(x=62,y=205)#texto
        self.pesquisaEdit.place(x=64,y=225)#quadrado
        self.btnBuscar.place(x=150,y=220)
        

        self.btnAlterar.place(x=350,y=115) #x=390,y=115
        self.btnExcluir.place(x=350,y=145) #x=390,y=115
        self.btnCadastrar.place(x=350,y=175) #x=390,y=115
        self.reuniaoList.place(x=60,y=250, height=180)  # x=60,y=250 , height=180 |(x=60,y=250)
        self.verscrlbar.place(x=485,y=250, height=180)#barra de rolagem (x=450,y=250, height=220)

        self.carregar_dados_iniciais_treeView()


    def carregar_dados_iniciais_treeView(self):
        registros = self.reuniaoCRUD.consultar()

        count = 0
        for item in registros:
            id = item[0]
            data = item[1]
            hora = item[2]
            assunto = item[3]

            self.reuniaoList.insert('','end',iid=count, values=(str(id),data,hora,assunto))
            count = count + 1


    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        data = self.dataEdit.get()
        hora = self.horaEdit.get()
        assunto = self.assuntoEdit.get("1.0",END)#para armazen texto com mais de uma linha colocar dentro de get "1.0",END
        #Chamar o cadastrar do departamento.py para cadastrar no banco
        #if self.departamentoCRUD.cadastrar(data,hora,assunto) == True:
        if self.reuniaoCRUD.cadastrar(data,hora,assunto):
            #Atualizar a TreeView           
           numeroLinhas = len(self.reuniaoList.get_children())
           id =  self.reuniaoCRUD.consultar_ultimo_id()
           self.reuniaoList.insert('','end',iid = numeroLinhas, values=(str(id),data,hora,assunto))
           mb.showinfo("Mensagem", "Cadastro executado com sucesso.")
            #Limpar os campos texto
           self.dataEdit.delete(0,tk.END)
           self.horaEdit.delete(0, tk.END) 
           self.assuntoEdit.delete("1.0",END)#para armazen texto com mais de uma linha colocar dentro de get "1.0",END
        else:
            mb.showinfo("Mensagem", "Erro no cadastro.") 
            self.dataEdit.focus_set()
            self.horaEdit.focus_set()
            self.assuntoEdit.focus_set()



    def _on_atualizar_clicked(self):
        linhaSelecionada = self.reuniaoList.selection()
      
        if len(linhaSelecionada) != 0:
            id= self.reuniaoList.item(linhaSelecionada[0])["values"][0]

            data = self.dataEdit.get()
            hora = self.horaEdit.get()
            assunto = self.assuntoEdit.get("1.0",END)

            if  self.reuniaoCRUD.atualizar(id,data,hora,assunto):

                self.reuniaoList.item(self.reuniaoList.focus(), values=(str(id),data,hora,assunto))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.dataEdit.delete(0, tk.END)
                self.horaEdit.delete(0, tk.END)
                self.assuntoEdit.delete("1.0", tk.END)
               
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")
                self.dataEdit.focus_set()
                self.horaEdit.focus_set()
                self.assuntoEdit.focus_set()



    def _on_deletar_clicked(self):
        linhaSelecionada = self.reuniaoList.selection()

        if len(linhaSelecionada) != 0:
            id = self.reuniaoList.item(linhaSelecionada[0])["values"][0]

            if  self.reuniaoCRUD.excluir(id):
                self.reuniaoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.dataEdit.delete(0, tk.END)
                self.horaEdit.delete(0, tk.END)
                self.assuntoEdit.delete("1.0", tk.END)
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.dataEdit.focus_set()   
                self.horaEdit.focus_set()    
                self.assuntoEdit.focus_set()   

    def _on_mostrar_clicked(self, event):#event e necessario para aparece dados epois que 
        selection = self.reuniaoList.selection()
        item = self.reuniaoList.item(selection[0])

        data = item["values"][1]
        hora = item["values"][2]
        assunto = item["values"][3]

        self.dataEdit.delete(0, tk.END)
        self.dataEdit.insert(0,data)

        self.horaEdit.delete(0, tk.END)
        self.horaEdit.insert(0,hora)

        self.assuntoEdit.delete("1.0", tk.END)#"1.0"para stringcomo mais de uma linha
        self.assuntoEdit.insert("1.0",assunto)#"1.0"para stringcomo mais de uma linha

   

    def _on_buscar_clicked(self):
        #id = self.pesquisaEdit.get()

        reuniao = Reuniao()
        self.resultado_reuniao = reuniao.consultar_por_id(id)
      
        self.reuniaoList.delete(*self.reuniaoList.get_children())
        #self.pesquisaEdit.insert('','end',iid=count, values=(str(id),data,hora,assunto))
        id = self.pesquisaEdit.get()

        count = 0
        for item in registros:
            id = item[0]
            data = item[1]
            hora = item[2]
            assunto = item[3]

            self.pesquisaEdit.insert('','end',iid=count, values=(str(id),data,hora,assunto))
            count = count + 1
       
        
        

        

#janela = tk.Tk()
#principal = ReuniaoView(janela)
#janela.title("Cadastro de Reuniao")
#janela.iconbitmap("imagens\icon.ico")
#janela.geometry("540x500+0+0")
#janela.mainloop()
