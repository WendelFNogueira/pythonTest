
# Chute um número

import sys
import random
import locale

x = random.randrange(1,10)
acertouMizeravi = 0

locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

def isNumber(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

print("Vamos brincar de 'Chute um Número'?\n")
querBrincar = (input("Sim / Não: "))

if not isNumber(querBrincar):
	if querBrincar=="sim":
		print("Beleza! Advinhe qual o número que eu tenho nas 'mãos'\n")
		print("É um número entre 1 - 10\n")
		print("Você pode fazer quantas tentativas quiser\n")
		while acertouMizeravi<1:
			try: 
				y = int(input("\nVou chutar: "))
			except ValueError:
				print("\n\nError: Invalid input.")
				sys.exit(1)
			if y < x:
				print("Tá esquentando! Mas ainda não é esse número!\n")
				print("Tenta um número maior ;)\n")
			elif y > x:
				print("Vish, passou direto! Tenta um número menor!\n")

			else:
				print("Parabéns! Você acertou!")
				acertouMizeravi=1
				print(f"\nResultado: {x}")
	else:
		print("\nEntão até uma próxima!")
else:
	print("\n\nError: Invalid input.")