import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 51, [4, 4])

print(mtz)

medias_linhas = mtz.mean(axis=1)
medias_colunas = mtz.mean(axis=0)

print(medias_linhas)
print(medias_colunas)

print(medias_linhas.max())
print(medias_colunas.max())

valores, quantidades = np.unique(mtz, return_counts=True)

for i in range(len(valores)):
    print(valores[i], quantidades[i])

print(valores[quantidades == 2])
