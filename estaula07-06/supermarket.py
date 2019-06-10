from peewee import *

db = SqliteDatabase('supermarket.db')

class Product():
    namProduct = CharField()
    valueProduct = FloatField()

class Item():
    product = ForeignKeyField(Product)
    amount = FloatField()

class Cart():
    denCart = CharField()

class CartItem():
    cart = ForeignKeyField(Cart)
    item = ForeignKeyField(Item)

class BaseModel(Model):
    class Meta:
        database = db



