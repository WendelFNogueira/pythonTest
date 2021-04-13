import turtle
import math

bob = turtle.Turtle()
print(bob)

#Função generalizada
def polyline(t, n, length, angle):
	"""Desenha n segmentos de reta com o comprimento dado
	e ângulo (em graus) entre eles. t é um turtle.
	"""
	for i in range(n):
		t.fd(length)
		t.lt(angle)


def square(t, length):
	"""
	Desenha um quadrado com a entrada das larguras dos lados
	t = turtle
	length = largura dos lados do quadrado
	"""
	angle = 90
	n = 1
	for i in range(n):
		t.lt(angle)
		t.fd(length)

	#polyline(t, n, length, angle)


def polygon(t, n, length):
	"""
	Desenha um polígonos regulares com n lados
	t = turtle
	n = número de lados
	length = largura dos lados
	"""
	angle = 360/n
	polyline(t, n, length, angle)
	for j in range(1):
		t.fd(85)


def arc(t, r, angle):
	"""
	Desenha um arco com o raio e o angulo passado no parametro
	t = turtle
	r = raio
	angle = ângulo (deve ser dado em graus)
	"""
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3)+1
	step_length = arc_length / n
	step_angle = float(angle) / n
	t.lt(step_angle/2)
	polyline(t, n, step_length, step_angle)
	t.rt(step_angle/2)


def circle(t, r):
	"""
	Desenha um círculo com o raio dado
	t = turtle
	r = raio
	"""
	arc(t, r, 360)


"""
Para o desenho ficar centralizado 

radius = 100
bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()
"""
polygon(bob, 3, 170)
circle(bob, 45)
square(bob, 90)
#Espera o usuário fechar a janela
turtle.mainloop()
