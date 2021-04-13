#Simulador de dados

import sys
import random

x = random.randrange(1,7)

def isNumber(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

print("Você gostaria de jogar o dado?\n")
resposta = (input("Sim / Não: "))

if not isNumber(resposta):
	if resposta =="sim":
		print(f"\nResultado: {x}")
	else:
		print("\nEntão até uma próxima!")
else:
	print("\n\nError: Invalid input.")

