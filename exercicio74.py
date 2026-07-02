# 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import cores
from random import randint

numLista = tuple(randint(1,100) for _ in range(5))
maior = menor = numLista[0]

print(numLista)

#for numero in numLista:
#    if numero > maior:
#        maior = numero
#
#    if numero < menor:
#        menor = numero

print(f'{cores.verde}↑{cores.fimCor}{max(numLista)} {cores.vermelho}↓{cores.fimCor}{min(numLista)}')