from peewee import *

class Ingrediente:
    Nome = CharField()

class Receita:
    Nome = CharField()
    ComoFazer = CharField()
    Ingrdientes = ForeignKeyField(Ingrediente)