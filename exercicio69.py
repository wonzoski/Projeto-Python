# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final mostre: 
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
import cores

contIdade = contM = contF = 0
corIdade = corSexoM = corSexoF = cores.vermelho

while True:
    idade = int(input('Digite a idade: '))

    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: M/F ')).strip().upper()[0]
    
    pergunta = input('Deseja continuar? S/N ').strip().upper()[0] == 'N'

    if idade > 18:
        contIdade += 1
        corIdade = cores.verde

    if sexo == 'M':
        contM += 1
        corSexoM = cores.verde
    
    if sexo == 'F' and idade < 20:
        contF += 1
        corSexoF = cores.verde

    if pergunta:
        break

print(f'{corIdade}→{cores.fimCor} {contIdade} tem mais de 18 anos\n{corSexoM}→{cores.fimCor} {contM} homens foram cadastrados\n{corSexoF}→{cores.fimCor} {contF} mulhere(s) tem menos de 20 anos.')