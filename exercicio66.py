# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)
import cores

número = 0
contador = 0
soma = 0

while True:
    número = int(input('Digite o número desejado: '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'O valor total de números digitados é: {cores.verde}{contador}{cores.fimCor}\nA somatória dos números é: {cores.azul}{soma}{cores.fimCor}')