# -*- coding: utf-8 -*-
def read_ranking(nome_arquivo, num):
    # nome_arquivo = "ranking0{}.txt".format(num)
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.readlines()

def make_a_list_of_all_rankings():
    return [read_ranking(num) for num in xrange(1, 8)]

def record_consenso_ranking(data):
    with open('resultado.txt', 'w') as f:
        for item in data:
            f.write(item)

# return tuple([read_ranking(num) for num in xrange(1, 8)])
# case tests
# a = ('a', 'b', 'c')
# b = ('b', 'c', 'd')
# c = ('a', 'b', 'd')

# L1 = ('a', 'b', 'c')
# L2 = ('d', 'e', 'c')

# with open('ranking01.txt', 'r') as arquivo:
#     L1 = arquivo.readlines()