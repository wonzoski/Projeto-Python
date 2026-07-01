# 076 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
import cores

lista_produtos_preco = ('Lápis', 1.75 , 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferido', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)

# print(lista_produtos_preco)

# print(f'{lista_produtos_preco[0]:.<40}')
print(f'{cores.vermelho}-'*53)
print(f'|'+' '*51+'|')
print(f'-'*53+f'{cores.fimCor}')
for pos, produto in enumerate(lista_produtos_preco):
    if pos % 2 == 0:
        print(f'{cores.vermelho}|{cores.fimCor} {produto:.<40}R$ ', end='')
    else:
        print(f'{produto:>6.2f} {cores.vermelho}|{cores.fimCor}')
print(f'{cores.vermelho}-{cores.fimCor}'*53)