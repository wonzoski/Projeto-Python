# 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000,00.
# C) Qual é o nome do produto mais barato.

import cores

totalProd = contMil = barato = 0
corBarato = corPreco = cores.vermelho

while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o valor do produto: R$'))

    pergunta = str(input('Deseja prosseguir? S/N')).strip().upper()[0] == 'N'

    # A) Qual é o total gasto na compra.
    totalProd += preço

    # B) Quantos produtos custam mais de R$ 1000,00.
    if preço > 1000:
        contMil += 1
        corPreco = cores.verde

    # C) Qual é o nome do produto mais barato.
    if preço > barato:
        nomeBarato = produto
        corBarato = cores.verde

    if pergunta:
        break

print(f'{cores.verde}→{cores.fimCor} Total gasto: R${totalProd:.2f}\n{corPreco}→{cores.fimCor} Produtos que custam mais de R$1000,00: {contMil}\n{corBarato}→{cores.fimCor} Produto mais barato: {nomeBarato}')