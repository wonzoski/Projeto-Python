# 063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
import cores

numero = int(input('Digite um número desejado: '))

contador = 1

primeiro_termo = 0
segundo_termo = 1
valor_real = 0

while contador <= numero:
    print(f'{cores.amarelo}{cores.negrito}->{cores.fimCor} {segundo_termo} ', end='', flush=True)
    valor_real = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = valor_real
    contador += 1
print(f'')