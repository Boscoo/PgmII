class Cliente:
    def __init__(self, nome, cpf, senha, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        return "Nome: " + self.nome + "\n" + "CPF: " + self.cpf + "\n" + "Senha: " + self.senha + "\n" + "Email: " +\
             self.email + "\n" + "Telefone: " + self.telefone + "\n"

class Animal:
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono
    
    def __str__(self):
        return "Nome: " + self.nome + "\n" + "Espécie: " + self.especie + "\n" + "Dono: " + self.dono.nome + "\n" 

class Produto:
    def __init__(self, codigo, preco, quantidade_estoque, nome_produto):
        self.codigo = codigo
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.nome_produto = nome_produto

class Consulta:
    def __init__(self, cliente, animal, tipo_atendimento, finalidade, horario_marcado, horario_executado):
        self.cliente = cliente
        self. animal = animal
        self.tipo_atendimento = tipo_atendimento
        self.finalidade = finalidade
        self.horario_marcado = horario_marcado
        self.horario_executado = horario_executado

c = Cliente("David", "08458426589", "123456", "fulano@servidor.com", "40028922")
a = Animal("Tóby", "preguiça", c)
p = Produto("1", "50", "85", "Folha")
o = Consulta(c, a, "alimentacao", "comer", "14", "14:20")

if __name__ == '__main__':
    print(c)
    print(a)