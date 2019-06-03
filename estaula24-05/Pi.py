class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome     = nome
        self.idade    = idade
        self.telefone = telefone

    def __str__(self):
        return "Nome: " + self.nome + ", Idade: " + str(self.idade) + ", Telefone: " + str(self.telefone)

class Aluno(Pessoa):
    def __init__(self, nome, idade, telefone, matricula, curso, turma):
        super().__init__(nome, idade, telefone)
        self.matricula = matricula
        self.curso     = curso
        self.turma     = turma

class Professor(Pessoa):
    def __init__(self, nome, idade, telefone, codProf, areas):
        super().__init__(nome, idade, telefone)
        self.codProf = codProf
        self.areas   = areas

class PI:
    def __init__(self, titulo, ano, nmAlunos, nmProf):
        self.titulo   = titulo
        self.ano      = ano
        self.nmAlunos = nmAlunos
        self.nmProf   = nmProf

class Periodicos:
    def __init__(self, ISSN, editora):
        self.ISSN    = ISSN
        self.editora = editora]

class Eventos:
    def __init__(self, data, local):
        self.data  = data
        self.local = local