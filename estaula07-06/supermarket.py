from peewee import *

db = 

class Produto():
    nomProduto = CharField()
    valorProduto = FloatField()

class Item():
    produto = ForeignKeyField(Produto)
    qtd = FloatField()

class Carrinho():
    denCarrinho = CharField()

class ItemdoCarrinho():
    carrinho = ForeignKeyField(Carrinho)
    item = ForeignKeyField(Item)

class BaseModel(Model):
    class Meta:
        database = db



