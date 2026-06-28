# 046 - Faça um programa que mostre na tela uma contegem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segungo entre eles.
import time
import cores

for count in range(10, -1, -1):
    if count > 5:
        cor = cores.amarelo
    else:
        cor = cores.vermelho
    print(f'Os fogos irão começa em {cores.negrito}{cor}{count}{cores.fimCor} segundos! ',end='\r')
    time.sleep(1)
print(f'{cores.amarelo}BUM **{cores.azul}*BUM {cores.vermelho}*POW *{cores.ciano}** *POW! *{cores.fimCor}' + ' '*30) 