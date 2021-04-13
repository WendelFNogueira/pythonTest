
# Escreva uma função que receba uma string como parâmetro
# e exiba a string com espaços suficientes à frente para 
# que a última letra da string esteja na coluna 70 da tela

def right_justify(s):
	for i in range(70):
		print(" ", end=" ")

	print(s)

right_justify("monty")
