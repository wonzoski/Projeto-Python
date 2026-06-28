# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Referência de tabela https://pt.wikipedia.org/wiki/Teorema_de_Wilson
import cores, math
print(f'{cores.backAzul}primos{cores.fimCor}')
print(f'{cores.backAmarelo}compostos{cores.fimCor}')
print(f'{cores.vermelho}-{cores.fimCor}' * 44)
for numero in range(2,31):
    if (math.factorial(numero-1) + 1) % numero == 0:
        cor = cores.backAzul
    else:
        cor = cores.backAmarelo    
    print(f'{cor}| {numero:>2} | {math.factorial(numero-1):>31} | {(math.factorial(numero-1) + 1) % numero} |{cores.fimCor}')
print(f'{cores.vermelho}-{cores.fimCor}' * 44)