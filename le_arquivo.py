# lista_de_listas = []
# for num in range(1, 3):
#     nome_arquivo = "ranking0%s.txt" % num
#     with open(nome_arquivo, 'r') as arquivo:
#         lista_de_listas.append(arquivo.readlines())

with open('ranking01.txt', 'r') as arquivo:
    L1 = arquivo.readlines()

with open('ranking02.txt', 'r') as arquivo:
    L2 = arquivo.readlines()

with open('ranking03.txt', 'r') as arquivo:
    L3 = arquivo.readlines()