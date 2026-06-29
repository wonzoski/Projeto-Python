# 071 - Crie um programa que simule o funcionamento de um caixa eletronico. No início, pergunte ao usuário qual será o valor a ser sacado. (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50,00, R$20,00, R$10,00 e R$1,00

import cores

while True:
    # pergunte ao usuário qual será o valor a ser sacado
    valorSaque = int(input('Digite o valor do saque: R$'))

    NCinquenta = valorSaque // 50

    NVinte = (valorSaque % 50) // 20

    NDez = ((valorSaque % 50) % 20) // 10

    NUm = (((valorSaque % 50) % 20) % 10) // 1

    break

print(f'→ Notas de R$50: {NCinquenta}\n→ Notas de R$20: {NVinte}\n→ Notas de R$10: {NDez}\n→ Notas de R$1: {NUm}')