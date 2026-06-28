# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
import cores, os
from time import sleep

Numero_Um_Usuario = int(input('Digite o primeiro número para operação desejada: '))
Numero_Dois_Usuario = int(input('Digite o segundo número para operação desejada: '))
Escolha_Usuario = 0

while Escolha_Usuario != 5:
    os.system('clear')
    print(f'Numeros escolhidos: {cores.ciano}{Numero_Um_Usuario} {cores.fimCor}e{cores.ciano} {Numero_Dois_Usuario}{cores.fimCor} ')
    Escolha_Usuario = int(input(
    '[1] - Somar\n' \
    '[2] - Multiplicar\n' \
    '[3] - Maior\n' \
    '[4] - Novos números\n' \
    '[5] - Sair do programa\n'
    ))

    match Escolha_Usuario:
        case 1:
            print(f'A soma de {Numero_Um_Usuario} + {Numero_Dois_Usuario} é {Numero_Um_Usuario + Numero_Dois_Usuario}')
        case 2:
            print(f'A multiplicação de {Numero_Um_Usuario} X {Numero_Dois_Usuario} é {Numero_Um_Usuario * Numero_Dois_Usuario}')
        case 3:
            if Numero_Um_Usuario > Numero_Dois_Usuario:
                print(f'{Numero_Um_Usuario} é maior que {Numero_Dois_Usuario}')
            elif Numero_Um_Usuario < Numero_Dois_Usuario:
                print(f'{Numero_Dois_Usuario} é maior que {Numero_Um_Usuario}')
            else:
                print(f'{Numero_Dois_Usuario} é igual á {Numero_Um_Usuario}')
        case 4:
            Numero_Um_Usuario = int(input('Digite o primeiro número para operação desejada: '))
            Numero_Dois_Usuario = int(input('Digite o segundo número para operação desejada: '))
        case _:
            if Escolha_Usuario == 5:
                print("Saindo do programa",end='')
                for _ in range(4):
                    print('.',end='',flush=True)
                    sleep(0.5)
                print('')
                break
            else:
                print('Opção não conhecida.')
    sleep(5)