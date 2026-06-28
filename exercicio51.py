# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
import cores

firstTerm = int(input('Digite o primeiro termo da PA: '))
reason = int(input('Digite a razão dessa PA: '))

for escolha in range(0,11):
    print(f'{escolha+1:>2}° termo: {firstTerm+(reason*escolha)}')