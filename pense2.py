
# Um objeto de função é um valor que pode ser atribuído a uma variável
# ou passado como argumento. Por exemplo, do_twice é uma função que toma
# um objeto de função como argumento e o chama duas vezes

def do_twice(f, loop):
	f()
	f()
	if loop==2:
		do_twice(f, 1)


def print_spam():
	print("spam")

def print_twice(bruce):
	print(bruce)
	print(bruce)


do_twice(print_spam, 2)

