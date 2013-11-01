import os

dir_path = "/Users/salvianoo/Dropbox/Rankings_Corel1000"

def return_paths(image_dir):
    paths = []
    for num_ranking in xrange(1, 8):
        ranking_file = "ranking0{}.txt".format(num_ranking)
        full_file_path = dir_path + "/" + image_dir + "/" + ranking_file
        paths.append(full_file_path)
    return paths

def read_ranking(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.readlines()

def make_a_list_of_rankings(arquivos_de_ranking):
    return [read_ranking(arquivo) for arquivo in arquivos_de_ranking]

def record_consenso_ranking(image_dir, data):
    full_path = dir_path + "/" + image_dir + "/" + 'resultado.txt'
    with open(full_path, 'w') as f:
        for item in data:
            f.write(item)
