from peewee import *

db = 

class Pessoa():
    nome = CharField()
    aluno = IntegerField()

class Aluno(Pessoa):
    matricula = CharField()

class Professor(Pessoa):
    nRegistro = CharField()

class BaseModel(Model):
    class Meta:
        database = db