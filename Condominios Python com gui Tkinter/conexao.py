import sqlite3

class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'condominios.db'
        try:
            conexao = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao

    def createTableReuniao(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS reuniao')

        sql = """CREATE TABLE IF NOT EXISTS reuniao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data text NOT NULL,
                    hora text NOT NULL,
                    assunto varchar NOT NULL);"""

        cursor.execute(sql)
        conexao.commit()


    def createTablecontrolecondominio(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS controlecondominio')

        sql = """CREATE TABLE IF NOT EXISTS controlecondominio (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf varchar NOT NULL,
                    nome varchar NOT NULL,
                    apartamento varchar NOT NULL,
                    telefone varchar NOT NULL);"""

        cursor.execute(sql)
        conexao.commit()

    def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        #self.createTableReuniao(conexao,cursor)
        self.createTablecontrolecondominio(conexao,cursor)

