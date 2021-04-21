minhaString = "O rato roeu a roupa do rei de roma"

minhaString = minhaString.replace("o rei", "a rainha")  #substituição na string
busca = minhaString.find("rainha")  #busca elemento específico na string e aponta a posição
print(busca)

minhaString = minhaString.split()   #separa os elementos da string
a = "Oi"
b = "tudo bem?"
concatenar = a+", "+b+"\n"
print(minhaString)
print(concatenar)
print(concatenar.strip())   #remove caracteres especiais
print(concatenar.lower())   #string minuscula
print(concatenar.upper())   #string maiscula

