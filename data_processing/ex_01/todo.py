# -*- coding: utf8


from collections import Counter # RECOMENDADO!


def conta_um_arquivo(fpath):
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                pass
        # Seu código para processar um arquivo
        # Apague o pass
        # Retorne um dicionário {palavra: contagem}
        pass


def reduz(contagens_1, contagens_2):
    # Apague o pass
    # Seu código aqui
    # Soma as contagens de dois dicionários
    pass