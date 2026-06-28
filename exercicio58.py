# ------------------------------------------------------------------------------------------
# 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# from random import randint
# from time import sleep
# 
# numero = int(input('Digite o número escolhido de 0 até 5: '))
# numero_aleatorio = randint(0,5)
# print('Pensando em um número entre 0 e 5 ...')
# sleep(2)
# 
# if  numero.is_integer() and 0 <= numero <= 5:
#     if numero == numero_aleatorio:
#         print('Você acertou! Parabens.')
#     else:
#         print(f'Uma pena! Eu escolhi o número {numero_aleatorio}')
# else:
#     print('O valor digitado é incorreto!')
# ------------------------------------------------------------------------------------------

# 058 - Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
import cores

Numero_Computador = randint(0,11)
contador = 0

while True:
    contador += 1
    Numero_Usuario = int(input("Digite um número desejado: "))
    print('Pensando',end='', flush=True)
    for itera in range(0,4):
        print(f'.',end='', flush=True)
        sleep(0.5)
    print('')
    
    if Numero_Usuario == Numero_Computador:
        print(f'{cores.negativo}{cores.verde}Acertou!{cores.fimCor}\n')
        break
    elif Numero_Usuario > Numero_Computador:
        print(f'{cores.negativo}{cores.vermelho}Incorreto. Número é menor!{cores.fimCor}\n')
        continue
    else:
        print(f'{cores.negativo}{cores.vermelho}Incorreto. Número é maior!.{cores.fimCor}\n')
        continue
print(f'Foi um total de {cores.negrito}{cores.amarelo}{contador}{cores.fimCor} palpites até acertar.')