from peewee import *

arq = './pessoas.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

if __name__ == '__main__':
    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao Paulo",
        endereco="Rua n0", telefone="3333-7070")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone)

