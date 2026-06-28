# 053 - Cre um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo | anotaram a data da maratona
import cores

frase = str(input('Digite uma frase qualquer: ')).lower().replace(' ','')
novaFrase = ''

for palavra in range(len(frase), 0, -1):
    novaFrase += frase[palavra-1]

print(f'{novaFrase}\n{frase}')

if novaFrase == frase:
    print('A frase descrita é um palíndromo.')
else:
    print('Não é um palíndromo.')

# print(frase[::-1])