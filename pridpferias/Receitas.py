from peewee import *

class Ingrediente:
    idIng = PrimaryKeyField()
    nome = CharField()

class Receita:
    idrec = PrimaryKeyField()
    nome = CharField()
    comoFazer = CharField()

class IngredienteDaReceita:
    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    quantidade = CharField()