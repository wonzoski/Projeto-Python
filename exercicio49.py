# ------------------------------------------------------------------------------------------- #
# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# numero_inteiro = int(input("Digite um número inteiro: "))
# numero_inteiro = 5
# for x in range(1,11):
#     print(f"{numero_inteiro}x{x}={numero_inteiro*x}")
# ------------------------------------------------------------------------------------------- #

# 049 - Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
import cores

numero = int(input('Digite um número desejado: '))

print(f'{cores.ciano}-{cores.fimCor}'*20+f'{cores.negrito}{cores.amarelo}\n   Tabuada de {numero}{cores.fimCor}\n'+f'{cores.ciano}-{cores.fimCor}'*20)
for x in range(1, 11):
    print(f'   {x:>2} X {numero} = {numero * x}')