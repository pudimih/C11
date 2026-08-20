import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1. Apresente a porcentagem de missões que deram certo
status_mission = dataset[1:, 7]
sucesso = status_mission[status_mission == 'Success']
porcentagem_sucesso = (len(sucesso) / len(status_mission)) * 100
print(f"1. Porcentagem de missões com sucesso: {porcentagem_sucesso:.2f}%")

# 2. Qual a media de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (>0)?
custos = dataset[1:, 6].astype(float)
custos_validos = custos[custos > 0]
media_gastos = custos_validos.mean()
print(f"2. Média de gastos das missões (valores > 0): {media_gastos:.2f}")

# 3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (EUA)
locais = dataset[1:, 2]
missoes_eua = locais[np.char.find(locais, 'USA') != -1]
print(f"3. Quantidade de missões realizadas pelos EUA: {len(missoes_eua)}")

# 4. Encontre qual foi a missão mais cara realizada pela empresa 'SpaceX'
empresas = dataset[1:, 1]
custos_spacex = custos[empresas == 'SpaceX']
missoes_spacex = dataset[1:, 4][empresas == 'SpaceX']
indice_mais_cara_spacex = custos_spacex.argmax()
missao_mais_cara_spacex = missoes_spacex[indice_mais_cara_spacex]
valor_mais_cara_spacex = custos_spacex[indice_mais_cara_spacex]
print(f"4. Missão mais cara da SpaceX: {missao_mais_cara_spacex} (Custo: {valor_mais_cara_spacex})")

# 5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões
empresas_unicas, quantidades = np.unique(empresas, return_counts=True)
print("5. Empresas e quantidade de missões:")
for empresa, qtd in zip(empresas_unicas, quantidades):
    print(f"   - {empresa}: {qtd}")
