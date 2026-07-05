# 087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma de todos os valores da terceira coluna.
# C) O maior valor da segunda linha.

import cores

matriz, linha = [], []
pares = 0

for x in range(3):
    for y in range(3):
        if x == 0:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: ')))
        if x == 1:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: ')))
        if x == 2:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: '))) 
    matriz.append(linha[:])
    linha.clear()


print(pares)