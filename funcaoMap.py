def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

#Rcebe dois argumentos
# map(função, lista)

valorDobrado = map(dobro, valor)
"""for v in valorDobrado:
    print(v)"""
valorDobrado = list(valorDobrado)
print(valorDobrado)