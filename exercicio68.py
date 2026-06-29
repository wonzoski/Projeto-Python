# 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
import cores
from random import randint
number = cont = 0 
while True:
    computerNumber = randint(1,10)

    menu = 3
    while 2 != menu != 1:    
        menu = int(input('1 - ÍMPAR\n2 - PAR\n'))

    number = int(input('Digite o número escolhido: '))

    total = number + computerNumber

    ganhou = (total % 2 == 0 and menu == 2) or (total % 2 != 0 and menu == 1)

    print(f'Número escolhido pelo computador {computerNumber}, o seu é {number}')

    if ganhou:
        cont += 1
        print(f'{cores.backVerde}Você venceu!{cores.fimCor} Número de vitórias consecutivas é: {cores.backVerde}{cont}{cores.fimCor}\n')
        continue
    else:
        print(f'{cores.backVemelho}Você perdeu!{cores.fimCor}. Número de vitórias: {cont}\n')
        break