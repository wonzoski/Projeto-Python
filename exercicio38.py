# 038 - Escreva um programa que leia dois números internos e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

numEscUm = int(input('Digite o primeiro número: '))
numEscDois = int(input('Digite o segundo número: '))
    
if numEscUm > numEscDois:
    print(f'\033[4;34m{numEscUm}\033[m é maior que \033[4;34m{numEscDois}\033[m')
elif numEscDois < numEscDois:
    print(f'\033[4;34m{numEscDois}\033[m é maior que \033[4;34m{numEscUm}\033[m')
elif numEscUm == numEscDois:
    print(f'\033[4;34m{numEscUm}\033[m é igual a \033[4;34m{numEscDois}\033[m')