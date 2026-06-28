# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# 061 - Refaça o desafio 051, lendo o primeito termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# import cores
#
#primeiro_termo = int(input('Digite o primeiro termo da PA: '))
#razao = int(input('Digite a razão dessa PA: '))
#
#contador = 0
#print(primeiro_termo)
#while contador != 9:
#    primeiro_termo += razao
#    print(primeiro_termo)
#    contador += 1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# 062 Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.
import cores

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

contador = 0
termos = 9

print(primeiro_termo)
while True:
    if contador != termos:
        primeiro_termo += razao
        print(primeiro_termo)
        contador += 1
        continue
    
    novos_termos = int(input('Deseja mostrar mais quantos termos? '))
    if novos_termos != 0:
        termos += novos_termos
        continue
    else:
        break