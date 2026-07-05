# 086 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
import cores

matriz, linha = [], []

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

for numero in matriz:
    print(f'{numero}')