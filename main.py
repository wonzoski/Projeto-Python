# 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
import cores

while True:
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        print('Masculino.')
        break
    elif sexo == 'F':
        print('Feminino.')
        break
    else:
        print(f'Valor {cores.backVemelho}não{cores.fimCor} corresponde ao solicitado!\n')
        continue