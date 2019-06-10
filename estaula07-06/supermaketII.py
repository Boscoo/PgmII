import os 
from peewee import *

db = SqliteDatabase('supm.py')

class Product():
    namProduct = CharField()
    valueProduct = FloatField()
    items = ManyToManyField(Item)

class Item():
    product = ForeignKeyField(Product)
    amount = FloatField()

class BaseModel(Model):
    class Meta:
        database = db

if os.path.exists('supm.py'):
    os.remove('supm.py')
db.connect()
db.create_tables([Product, Item, Product.items.get_through_model()])
x = Product.create(namProduct = "Rice", valueProduct = 5.00)
y = Item.create()