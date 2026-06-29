# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
import cores

numero = 0 

while True:
    numero = int(input('Digite o número desejado: '))
    if numero < 0:
        break
    
    for x in range(1,11):
        print(f'{cores.backAmarelo}{numero}{cores.fimCor} X {x:>2} = {cores.backVemelho}{numero*x}{cores.fimCor}')
    