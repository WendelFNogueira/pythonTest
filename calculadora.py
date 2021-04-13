#Projeto simples de uma calculadora

#Importando arquivos do sistema operacional
#Para usar a função de limpar tela
import os

#Importando função para a parada do sistema
#caso seja necessário
import sys

#Importando internacionalização 
#para formatar todo o texto em pt-br
import locale
locale.setlocale(locale.LC_ALL,"Portuguese_Brazil.1252")

#Definindo uma função para verificar se o input é válido
def isNumber(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

#criando variável
escolha = str

while(escolha != 's'):
	#Função de limpar a tela
	os.system("clear") or None
	#Criando um menu
	print('Bem Vindo A Calculadora Tutu!\n\n')
	print('\nOque você deseja? escolha entre:') # O "\n" causa quebra de linha
	print("(+) - Adição")
	print("(-) - Substração")
	print("(/) - Divisão")
	print("(*) - Multiplicação")
	print("(s) - Sair")
	print("*ATENÇÃO* Digite pelo simbolo da operação!")
	escolha = input("\nDigite sua opção: ")	
	# A condição a seguir se lê:
	# Se *escolha* NÃO é número, então:
	if not isNumber(escolha):
		if escolha == 's':
			print("Até logo!")
			sys.exit(1)
		else:
			x = int(input('\n\nPrimeiro número: '))
			y = int(input('\nSegundo número: '))
			if isNumber(x):
				if isNumber(y):
					if escolha == "+":
						resultado = x + y
						print(f"\n{x} + {y} = {resultado}")
					elif escolha == "-":
						resultado = x - y
						print(f"\n{x} - {y} = {resultado}")
					elif escolha == "/":
						resultado = x / y
						print(f"\n{x} / {y} = {resultado}")
					elif escolha == "*":
						resultado = x * y
						print(f"\n{x} * {y} = {resultado}")
					else:
						print("\nDigite uma opção válida!")
				else:
					print("\nError: Input inválido! Use somente números inteiros.")
			input("\nTecle ENTER para continuar") # Um input apenas para dar pausa ao programa
	else:
		print("\nError: Input inválido! Use somente strings.")
