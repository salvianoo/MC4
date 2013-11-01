# -*- coding: utf-8 -*-
from acessar_pastas import return_paths, make_a_list_of_rankings, record_consenso_ranking
from mc4 import mc4

dir_paths = os.listdir(dir_path)
del dir_paths[0]  ## Remove .DS_Store dir

for image_dir in dir_paths:
    arquivos_de_ranking = return_paths(image_dir)
    rankings = make_a_list_of_rankings(arquivos_de_ranking)
    ranking_consenso = mc4(rankings)
    record_consenso_ranking(image_dir, ranking_consenso)

# rankings = make_a_list_of_all_rankings()
# ranking_consenso = mc4(rankings)
# record_consenso_ranking(ranking_consenso)