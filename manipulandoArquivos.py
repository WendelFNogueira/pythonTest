arquivo = open("arquivoTeste.txt")

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)