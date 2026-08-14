import numpy as np

mtz = np.zeros([2, 2])

linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)

mtz[linha, coluna] = 1

jogadas = 0

while jogadas < 3:
    linha_jogada = int(input("Digite a linha (0 ou 1): "))
    coluna_jogada = int(input("Digite a coluna (0 ou 1): "))

    if mtz[linha_jogada, coluna_jogada] == 1:
        print("Game Over! : ( Try Again!")
        break

    jogadas += 1

if jogadas == 3:
    print("Congratulations! You beat the game! :)")
