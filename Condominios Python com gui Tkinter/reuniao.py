import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Reuniao:

    def cadastrar(self,data,hora,assunto):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO reuniao (data,hora,assunto) VALUES (?,?,?)'
            cursor.execute(sql,[data,hora,assunto])
    
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de reunião: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM reuniao').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consultar_detalhes(self, id):  
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute('SELECT * FROM reuniao WHERE id = ?', (id,)).fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        

        cursor.close()
        conexao.close()
        return resultset


    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(id) FROM reuniao').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id, data, hora, assunto):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE reuniao SET data = ?, hora = ?, assunto = ?  WHERE id = (?)'
            cursor.execute(sql,(data,hora,assunto,id))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de reunião: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False


    def excluir(self,id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM reuniao WHERE id = (?)'
            cursor.execute(sql,[id])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de reunião: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False


    #def consultar_por_id(self,id):
    def consultar_por_data(self,data):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        data = self.transforma_data(data)

        sql = """SELECT r.id, r.data, r.hora, r.assunto   
                    FROM reuniao as r 
                    WHERE r.data = ?
                    ORDER BY r.data"""

        try:
            resultset =  cursor.execute(sql,[data]).fetchall()
        except sqlite3.Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset    
    
    def transforma_data(self, data):
        data = data.split("/")
        data = data[2].lstrip("0") + "-" + data[1].lstrip("0") + "-" + data[0].lstrip("0")
        return data

    def consultar_por_id(self, id):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()



        #sql = """SELECT r.id, r.data, r.hora, r.assunto   
                    #FROM reuniao as r 
                    #WHERE r.id = ?
                   # ORDER BY r.id""" 

        sql = """SELECT id, data, hora, assunto 
                 FROM reuniao
                 WHERE id = ? 
                 ORDER BY id"""

        try:
            resultset =  cursor.execute(sql,[id]).fetchall()
        except sqlite3.Error as e:
            print(f"O erro '{e}' ocorreu.")

            

        cursor.close()
        conexao.close()
        return resultset    