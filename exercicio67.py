# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
import cores
numero = 0 
while True:
    numero = int(input('Digite o número desejado: '))
    if numero < 0:
        break
    for x in range(1,11):
        if x % 2 == 0:
            corLinha = cores.backAmarelo
        else:
            corLinha = cores.backAzul
        print(f'{corLinha}{numero} X {x:<2} = {numero*x}{cores.fimCor}')