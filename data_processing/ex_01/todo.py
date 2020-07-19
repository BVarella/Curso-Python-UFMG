# -*- coding: utf8


from collections import Counter


def conta_um_arquivo(fpath):
    cnt = Counter()

    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split()
                for palavra in palavras:
                    cnt[palavra] += 1

    return dict(cnt)


def reduz(contagens_1, contagens_2):
    return Counter(contagens_1) + Counter(contagens_2)
