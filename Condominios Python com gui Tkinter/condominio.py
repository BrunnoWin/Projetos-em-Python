import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Condominio:
    def cadastrar(self,cpf,nome,apartamento,telefone):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO controlecondominio (cpf,nome,apartamento,telefone) VALUES (?,?,?,?)'
            cursor.execute(sql,[cpf,nome,apartamento,telefone])
    
           
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
            resultset =  cursor.execute('SELECT * FROM controlecondominio').fetchall()
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
            resultset = cursor.execute('SELECT MAX(id) FROM controlecondominio').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]

    def atualizar(self,id, cpf, nome, apartamento, telefone):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE controlecondominio SET cpf = ?, nome = ?, apartamento = ?,telefone = ?  WHERE id = (?)'
            cursor.execute(sql,(cpf,nome,apartamento,telefone,id))
           
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

            sql = 'DELETE FROM controlecondominio WHERE id = (?)'
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



