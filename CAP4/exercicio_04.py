import numpy as np

mtz = np.array([[1, 2, 3], [4, 5, 6]])

linhas = mtz.shape[0]
colunas = mtz.shape[1]

quantidade = linhas * colunas

if quantidade % 2 == 0:
    print("A matriz poderia se tornar um vetor unidimensional com número par de elementos.")
else:
    print("A matriz poderia se tornar um vetor unidimensional com número ímpar de elementos.")
