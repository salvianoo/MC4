# -*- coding: utf-8 -*-

# a = ('a', 'b', 'c')
# b = ('b', 'c', 'd')
# c = ('a', 'b', 'd')

L1 = ('a', 'b', 'c')
L2 = ('d', 'e', 'c')

# gera U aplicando a funcao de uniao
def set_U(*rankings):
    cast = lambda ranking: set(ranking)
    rankings = map(cast, rankings)
    U = reduce(set.union, rankings)
    return sorted(U)

def have_both(pair_ij, rank):
    i = pair_ij[0]
    j = pair_ij[1]
    return i in rank and j in rank

# verifica se o j e maior q i. ("a", "b")
def checkj_above_i(pair_ij, rank):
    i, j = pair_ij
    try:
        if rank.index(j) < rank.index(i):
            return True
        else:
            return False
    except ValueError:
        return False

def check(pair_ij, *rankings):
    ambos = 0
    j_above_i = 0

    for rank in rankings:
        if have_both(pair_ij, rank):
            ambos += 1

        if checkj_above_i(pair_ij, rank):
            j_above_i += 1

    if ambos == 0: # quando o par nao é classificado em nenhum ranking
        return 0.5
    else:
        return j_above_i / ambos

U = set_U(L1, L2)
size_u = len(U)

M = [[(y, x) for x in U] for y in U]
T = [[0 for x in U] for y in U]

for i in xrange(size_u):
    for j in xrange(size_u):
        if i != j:
            item = M[i][j]
            M[i][j] = check(item, L1, L2)
        else:
            M[i][j] = 0
print M

for i in xrange(size_u):
    for j in xrange(size_u):
        if i != j:
            T[i][j] = M[i][j] / size_u
        else:
            somatorio = sum(M[i]) / size_u
            T[i][j] = (1.0 - somatorio)
print T

dict_ranking = {k: 0 for k in U}
diagonal = []

for i in xrange(size_u):
    for j in xrange(size_u):
        if i == j:
            diagonal.append(T[i][j])

for k, v in zip(U, diagonal):
    dict_ranking[k] = v

import operator
ranking = sorted(dict_ranking.iteritems(), key=operator.itemgetter(1), reverse=True)
ranking = map(lambda x: x[0], ranking)
print ranking