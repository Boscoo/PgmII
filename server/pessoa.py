class Pessoa():
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def arquivar(self):
    	file = open("file.txt", "a")
    	file.write(self.nome + ";" + self.endereco + ";" + self.telefone + "\n")
    	return True 

    def actualizar(self):
    	file = open("file.txt", "r")
    	linhas = file.readlines()
    	for lin in linhas:
    		pessoas = lin.split(";")
    		print(pessoas)
    		
    		
    	# pessoa = pessoas[-1].split("\n")
    	# print(pessoa)
    	# self.nome = pessoa[0]
    	# self.endereco = pessoa[1]
    	# self.telefone = pessoa[2]
    	return True