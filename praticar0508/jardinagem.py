from peewee import *
import os

arq = "jardim.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Jardim(BaseModel):
    nome = CharField()
    def __str__(self):
        return "Nome: " + self.nome

class Planta(BaseModel):
    nome = CharField()
    nomeCi = CharField()
    tamanhoF = CharField()
    periodoDePoda = IntegerField()
    dataDePoda = DateField()
    def __str__(self):
        return "Nome: " + self.nome + "\n" + "Nome científico: " + self.nomeCi

class PlantasDoJardim(BaseModel):
    jardim = ForeignKeyField(Jardim)
    planta = ForeignKeyField(Planta)
    def __str__(self):
        return "Nome do jardim: " + self.jardim.nome + "\n" + "Nome da Planta: " + self.planta.nome  


if __name__ == '__main__':
    
    if os.path.exists(arq):
        os.remove(arq)

db.connect()
db.create_tables([Jardim, Planta, PlantasDoJardim])
jardim1 = Jardim.create(nome="Jardim da Luz")
marg = Planta(nome="Margarida", nomeCi="Leucanthemum vulgare", tamanho="Pequena", periodoDePoda="120", dataDePoda="2019-08-05")
plantajardim = PlantasDoJardim(jardim=jardim1, planta=marg)
print(plantajardim)