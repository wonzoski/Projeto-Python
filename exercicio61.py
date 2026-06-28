# --------------------------------------------------------------------------------------------------------------------------------------------
# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
#import cores
#
#firstTerm = int(input('Digite o primeiro termo da PA: '))
#reason = int(input('Digite a razão dessa PA: '))
#
#for escolha in range(0,11):
#    print(f'{escolha+1:>2}° termo: {firstTerm+(reason*escolha)}')
# --------------------------------------------------------------------------------------------------------------------------------------------

# 061 - Refaça o desafio 051, lendo o primeito termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
import cores

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

contador = 0
print(primeiro_termo)
while contador != 9:
    primeiro_termo += razao
    print(primeiro_termo)
    contador += 1