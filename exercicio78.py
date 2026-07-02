# 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

import cores
from random import randint

lista_numero = list(randint(0,100) for _ in range(5))

print(lista_numero)

print(f'O maior valor da lista é {max(lista_numero)} na posição {lista_numero.index(max(lista_numero))}.\nO menor valor da lista é {min(lista_numero)} na posição {lista_numero.index(min(lista_numero))}.\n')