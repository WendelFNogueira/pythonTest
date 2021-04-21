lista1 = [1, 2, 3, 4, 5]
lista2 = ["abelha", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00","R$5,00","R$7,00","R$10,00","R$15,00",]

for indice, nome, valor in zip(lista1, lista2, lista3):
    print(indice, nome, valor)