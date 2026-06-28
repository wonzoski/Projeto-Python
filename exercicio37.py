# 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numThis = int(input('Digite o número escolhido: \n'))
numEscolha = int(input('Escolha a base de conversão\n' \
'1 - Binário\n' \
'2 - Octal\n' \
'3 - Hexadecimal\n'))

if numEscolha == 1:
    binario = bin(numThis)[2:]
    print(f'Binário de \033[4;34m{numThis}\033[m é \033[4;33m{binario}\033[m')
elif numEscolha == 2:
    octal = oct(numThis)[2:]
    print(f'Octal de \033[4;34m{numThis}\033[m é \033[4;33m{octal}\033[m')
elif numEscolha == 3:
    hexadecimal = hex(numThis)[2:]
    print(f'Hexadecimal de \033[4;34m{numThis}\033[m é \033[4;33m{hexadecimal}\033[m')
else:
    print('\033[31mOpção inválida!\033[m')