import cores

print(f'{cores.backVemelho}As tuplas são imutáveis, só é permitido apagar ela inteira!{cores.fimCor}\n')

lanche = ('Hambúrger','Suco','Pizza','Pudim')

# Apagando tupla
print(f'{cores.verde}# Apagando tupla{cores.fimCor}')
print('del(lanche)')
print('')

# Capturando o valor da tupla
print(f'{cores.verde}# Capturando o valor da tupla{cores.fimCor}')
print(len(lanche))
print('')

# Sorteando os valores em ordem alfabética
print(f'{cores.verde}# Ordenando os valores em ordem alfabética{cores.fimCor}')
print(sorted(lanche))
print('')

# Método padrão de mostragem de valores de tupla:
print(f'{cores.verde}# Método padrão de mostragem de valores de tupla{cores.fimCor}')
for comidas in lanche:
    print(comidas)
print('')

# Método com valoração de range:
print(f'{cores.verde}# Método com valoração de range{cores.fimCor}')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('')

# Método usando enumerate:
print(f'{cores.verde}# Método usando enumerate{cores.fimCor}')
for pos, comida in enumerate(lanche, start=0): # O valor do contador pode ser alterado atravpes do "start=valor"
    print(f'Vou comer {comida} na posição {pos}')
print('')

# Juntando duas tuplas:
print(f'{cores.verde}# Juntando duas tuplas{cores.fimCor}')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print('')

# Contando quantia de valores existentes
print(f'{cores.verde}# Contando quantia de valores existentes{cores.fimCor}')
print(f'O número 5 aparece {cores.amarelo}{c.count(5)}{cores.fimCor} vezes.')
print('')

# Capturando posição de um valor
print(f'{cores.verde}# Capturando posição de um valor{cores.fimCor}')
print(f'O número 8 está na posição {cores.amarelo}{c.index(8)}{cores.fimCor} da tupla.') # Só irá aparecer a primeira ocorrência, para ocorrencias seguimtes deve usar c.index(5, 1) por exemplo.
print('')