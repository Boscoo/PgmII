import mysql.connector as connector

class FabricaDeConexao():
    __USUARIO = "root"
    __SENHA = "root"
    __DB_ADRESS = "localhost"
    __DATABASE = "pessoa"

    def __init__(self):
        self.con = None
        self.cursor = None

    def abrirConexao(self):
        if self.con is None:
            try:
                self.con = connector.connect(user = self.__USUARIO,
                                             password = self.__SENHA,
                                             host=self.__DB_ADRESS,
                                             database=self.__DATABASE)
                self.cursor = self.con.cursor()
            except connector.Error as err:
                print(err)
                self.con = None
                self.cursor = None

    def fecharConexao(self):
        try:
            self.con.commit()
            self.cursor.close()
            self.con.close()
            self.cursor = None
            self.con = None
        except connector.Error as err:
            print(err)

class Pessoa():
	def __init__(self, nome, endereco, telefone):
		self.n_registro = None
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone
    
    def gerar_nrg(self):
        for i in range (100):
            if self.n_registro == None:
                self.n_registro = i
            else: 
                break
    
class PessoaDAO():
    def __init__(self):
        self.fab = FabricaDeConexao()

    def criarTabela(self):
        sql_verificar_existencia_da_tabela = "SHOW TABLE LIKE 'pessoa'"
        self.fab.abrirConexao()
        self.fab.cursor.execute(sql_verificar_existencia_da_tabela)
        resultado = self.fab.cursor.fetchone()
        if resultado is None:
            sql_criar_tabela = """
                    CREATE TABLE pessoa (
                        n_registro INTEGER(3) NOT NULL,
                        nome VARCHAR(50) NOT NULL,
                        endereco VARCHAR(100) NOT NULL,
                        telefone VARCHAR(15) NOT NULL,
                        PRIMARY KEY(n_registro))
                    """
            self.fab.cursor.execute(sql_criar_tabela)
        self.fab.fecharConexao()

    def deletarTabela(self):
        sql_deletar_tabela = "DROP TABLE pessoa"
        self.fab.abrirConexao()
        self.fab.cursor.execute(sql_deletar_tabela)
        self.fab.fecharConexao()

    def buscartodos(self):
        sql_buscar = "SELECT * FROM pessoa"
        self.fab.abrirConexao()
        self.fab.cursor.execute(sql_buscar)
        results = self.fab.cursor.fetchall()
        lista = []
        while results:
            for ocorrencia in results:
                p = Pessoa(ocorrencia[0], ocorrencia[1], ocorrencia[2], ocorrencia[3])
                lista.append(p)
            results = self.fab.cursor.fetchall()
        self.fab.fecharConexao()
        return lista

    def salvarPessoa(self, pessoa):
        sql_salvar = "INSERT INTO pessoa (n_registro, nome, endereco, telefone) VALUES (%s, %s, %s, %s)"
        dados = (pessoa.n_registro, pessoa.nome, pessoa.endereco, pessoa.telefone)
        self.fab.abrirConexao()
        self.fab.cursor.execute(sql_salvar, dados)
        self.fab.fecharConexao()

    def updatePessoa(self, pessoa):
        sql_update = "UPDATE pessoa SET nome = %s, endereco = %s, telefone = %s WHERE n_registro = %s"
        dados = [pessoa.nome, pessoa.endereco, pessoa.telefone, pessoa.n_registro]
        self.fab.abrirConexao()
        self.fab.cursor.execute(sql_update, dados)
        self.fab.fecharConexao()

