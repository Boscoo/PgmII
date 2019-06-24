import os
from peewee import *
arq = 'bd.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta:
		database = db

class Pessoa(BaseModel):
	nome = CharField()
	endereco = CharField() 
	telefone = CharField()

if os.path.exists(arq):
	os.remove(arq)

db.connect()
db.create_tables([Pessoa])
