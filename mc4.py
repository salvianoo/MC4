# -*- coding: utf-8 -*-
import operator

def mc4(rankings):
    U = set_U(rankings)
    size_u = len(U)

    M = [[(y, x) for x in U] for y in U]
    T = [[0 for x in U] for y in U]

    for i in xrange(size_u):
        for j in xrange(size_u):
            if i != j:
                item = M[i][j]
                M[i][j] = check(item, rankings)
            else:
                M[i][j] = 0

    for i in xrange(size_u):
        for j in xrange(size_u):
            if i != j:
                T[i][j] = M[i][j] / float(size_u)
            else:
                somatorio = sum(M[i]) / float(size_u)
                T[i][j] = (1.0 - somatorio)

    dict_ranking = {k: 0 for k in U}
    diagonal = []

    for i in xrange(size_u):
        for j in xrange(size_u):
            if i == j:
                diagonal.append(T[i][j])

    for k, v in zip(U, diagonal):
        dict_ranking[k] = v

    ranking = sorted(dict_ranking.iteritems(), key=operator.itemgetter(1), reverse=True)
    return map(lambda x: x[0], ranking)

# gera U aplicando a funcao de uniao
def set_U(rankings):
    cast = lambda ranking: set(ranking)
    rankings = map(cast, rankings)
    U = reduce(set.union, rankings)
    return sorted(U)

def have_both(pair_ij, rank):
    i, j = pair_ij
    return i in rank and j in rank

# verifica se o j e maior q i. ("a", "b")
def checkj_above_i(pair_ij, rank):
    i, j = pair_ij
    try:
        return rank.index(j) < rank.index(i)
    except ValueError:
        return False

def check(pair_ij, rankings):
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
