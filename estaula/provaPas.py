lista = ["João de Oliveira", "Maria da Silva","Teresa Mattos", "Paulo José Có", "Jorge Lacerda", "Maria Rick Jou"]
def buscar(lista, busca):
	for i  in range(len(lista)):
		if busca.upper() in lista[i].upper():
			print(lista[i] + " " + str(i))

def contar(lista):
	quantidade = []
	for pessoa in lista:
		listaNomes = pessoa.split(" ")
		for i in range(len(listaNomes)):
			cont = 0
			for p in lista:
				ps = p.split(" ")
				for j in range(len(ps)):
					if listaNomes[i] == ps[j]:
						cont += 1
						quantidade.append((listaNomes[i], cont))
						if cont > 1:
							quantidade.insert(0, (listaNomes[i]	, cont))
	return dict(quantidade)


if __name__ == "__main__":

	buscar(lista, "d")
	print(contar(lista))