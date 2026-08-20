import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 6. Qual a porcentagem de missões realizadas com foguetes cujo status é "StatusRetired" (coluna Status Rocket)?
status_rocket = dataset[1:, 5]
foguetes_aposentados = status_rocket[status_rocket == 'StatusRetired']
porcentagem_aposentados = (len(foguetes_aposentados) / len(status_rocket)) * 100
print(f"6. Porcentagem de missões com foguetes 'StatusRetired': {porcentagem_aposentados:.2f}%")

# 7. Quantas missões foram lançadas a partir de localizações que contêm "Russia" (coluna Location)?
locais = dataset[1:, 2]
missoes_russia = locais[np.char.find(locais, 'Russia') != -1]
print(f"7. Quantidade de missões lançadas a partir da Rússia: {len(missoes_russia)}")

# 8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.
empresas = dataset[1:, 1]
custos = dataset[1:, 6].astype(float)
indice_mais_cara = custos.argmax()
empresa_mais_cara = empresas[indice_mais_cara]
valor_mais_cara = custos[indice_mais_cara]
print(f"8. Missão mais cara do dataset foi realizada pela {empresa_mais_cara} com valor de {valor_mais_cara}")
