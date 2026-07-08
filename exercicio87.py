# 087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma de todos os valores da terceira coluna.
# C) O maior valor da segunda linha.

import cores

matriz, linha = [], []
pares = soma_coluna = 0

for x in range(3):
    for y in range(3):
        if x == 0:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: ')))
        if x == 1:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: ')))
        if x == 2:
            linha.append(int(input(f'Digite o valor para [{x}, {y}]: ')))
        if linha[y] % 2 == 0:
            pares += linha[y]
        if y == 2:
            soma_coluna += linha[y]
    matriz.append(linha[:])
    linha.clear()

print(matriz)
print(f'A soma de todos os números pares digitados é {pares}')
print(f'A soma de todos os valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')