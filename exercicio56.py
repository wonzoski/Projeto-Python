# 056 - Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.
import cores

Idade_Soma = 0
Idade_Dif_Velho = 0
Nome_Mais_Velho = 'nda'
Contador_Mulher = 0

for _ in range(4):
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo: '))
    idade = int(input('Digite a idade: '))

    if sexo == 'masculino' and Idade_Dif_Velho < idade:
        Idade_Dif_Velho = idade
        Nome_Mais_Velho = nome

    if sexo == 'feminino' and idade < 20:
        Contador_Mulher += 1

    Idade_Soma += idade

print(f'A média de idade do grupo é de {Idade_Soma/4} anos.')

if Nome_Mais_Velho != 'nda':
    print(f'O nome do homem mais velho é {Nome_Mais_Velho}.')
else:
    print('Nenhum homem no grupo.')

if Contador_Mulher == 1:
    print("Apenas 1 mulher tem menos de 20 anos.")
elif Contador_Mulher > 1:
    print(f'{Contador_Mulher} mulheres tem menos de 20 anos.')
else:
    print('Nenhuma mulher com menos de 20 anos.')