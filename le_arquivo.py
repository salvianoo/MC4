# -*- coding: utf-8 -*-
def read_rankings_and_generate_lists():
    for num in xrange(1, 8):
        nome_arquivo = "ranking0{}.txt".format(num)
        with open(nome_arquivo, 'r') as arquivo:
            globals()['L{}'.format(num)] = arquivo.readlines()

read_rankings_and_generate_lists()

def grava_ranking(data):
    with open('resultado.txt', 'w') as f:
        for item in data:
            f.write(item)

# case tests
# a = ('a', 'b', 'c')
# b = ('b', 'c', 'd')
# c = ('a', 'b', 'd')

# L1 = ('a', 'b', 'c')
# L2 = ('d', 'e', 'c')

# with open('ranking01.txt', 'r') as arquivo:
#     L1 = arquivo.readlines()