# 088 - Faça um programa que ajude um jogar da mega sena. a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import cores
from random import sample

lista_numeros , dados = [], []

pergunta = int(input('Quantas jogadas deseja fazer? '))

for x in range(pergunta):
    dados.extend(sample(range(1,61),6))
    lista_numeros.append(dados[:])
    dados.clear()
    print(f'Jogo {x+1}: {sorted(lista_numeros[x])}')