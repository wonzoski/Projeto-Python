# 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão:       5% de desconto
# - Em até 2x no cartão:     preço normal
# - 3x ou mas no cartão:     20% de juros

import os, cores

valorTotal = float(input('\nDigite o valor total do(s) produto(s): \033[32mR$'))
metodoPagamento = int(input(f'\n{cores.ciano}-------- Forma de pagamento --------\n{cores.fimCor}' \
'  1 - À vista dinheiro/cheque\n' \
'  2 - À vista no cartão\n' \
'  3 - Em até 2x no cartão\n' \
'  4 - 3x ou mas no cartão\n' +\
f'{cores.ciano}-{cores.fimCor}' * 36 + '\n'))

if metodoPagamento == 1:
    print(f'Valor total a ser pago: {cores.amarelo}R${valorTotal - (0.10 * valorTotal):.2f}{cores.fimCor}')
elif metodoPagamento == 2:
    print(f'Valor total a ser pago: {cores.amarelo}R${valorTotal - (0.05 * valorTotal):.2f}{cores.fimCor}')
elif metodoPagamento == 3:
    print(f'Valor total a ser pago: {cores.amarelo}R${valorTotal:.2f}{cores.fimCor} parcelado em 2 vezes de {cores.amarelo}R${valorTotal/2:.2f}{cores.fimCor}')
elif metodoPagamento == 4:
    valorReal = valorTotal + (0.20 * valorTotal)
    parcela = int(input('Parcelado em quantas vezes? '))
    print(f'Valor total a ser pago: {cores.amarelo}R${valorReal:.2f}{cores.fimCor} parcelado em {cores.amarelo}{parcela}{cores.fimCor} vezes de {cores.amarelo}R${valorReal/parcela:.2f}{cores.fimCor}')
else:
    print(f'\n{cores.vermelho}Opção inválida!{cores.fimCor}')

