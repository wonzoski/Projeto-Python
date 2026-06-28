# 064 - Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final. mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)
import cores

acumulador = []

while True:
    numero = int(input('Digite o número desejado: '))
    if numero != 999:
        acumulador.append(numero)
    else:
        break
print(sum(acumulador))