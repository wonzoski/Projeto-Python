# 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

numero = int(input('Digite o número escolhido de 0 até 5: '))
numero_aleatorio = randint(0,5)
print('Pensando em um número entre 0 e 5 ...')
sleep(2)

if  numero.is_integer() and 0 <= numero <= 5:
    if numero == numero_aleatorio:
        print('Você acertou! Parabens.')
    else:
        print(f'Uma pena! Eu escolhi o número {numero_aleatorio}')
else:
    print('O valor digitado é incorreto!')