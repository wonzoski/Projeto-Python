import cores

from random import randint

lanche = ['Hamburguer','Suco','Pizza','Pudim']

# Adicionando valores no final da lista.
print(f' 1  {cores.verde}# Adicionando valores no final da lista.{cores.fimCor}')
print(f" 2    {cores.backAzul} {cores.fimCor} {cores.azul}lanche.append('Cookie'){cores.fimCor}")
lanche.append('Cookie')
print(f' 3  Resultado → {lanche}\n 4')

# Adicinando um valor em posição específica.
print(f' 5  {cores.verde}# Adicinando um valor em posição específica.{cores.fimCor}')
print(" 6  lanche.insert(0, 'Cachorro quente')")
lanche.insert(0, 'Cachorro quente')
print(f' 7  {lanche}\n 8')

# Eliminando valores através do índice.
print(f' 9  {cores.verde}# Eliminando valores através do índice.{cores.fimCor}')
print(f"10  del lanche[3]")
print(f"11  lanche.pop(3)")
del lanche[3]
lanche.pop(3)
print(f'12  {lanche}\n')

# Removendo com base no valor.
print(f'{cores.verde}# Removendo com base no valor.{cores.fimCor}')
lanche.remove('Cookie') # Remove apenas a primeira ocorrência
print(f'{lanche}\n')

# Removendo último elemento.
print(f'{cores.verde}# Removendo último elemento{cores.fimCor}')
lanche.pop()
print(f'{lanche}\n')

# Removendo mas confirmando antes.
if 'Pizza' in lanche:
    lanche.remove('Pizza')

# Enumerate.
print(f'{cores.verde}# Método usando enumerate{cores.fimCor}')
for pos, comida in enumerate(lanche, start=0): # O valor do contador pode ser alterado atravpes do "start=valor"
    print(f'Vou comer {comida} na posição {pos}')
print('')

# Criando lista de valores aleatórios.
print(f'{cores.verde}# Criando lista de valores aleatórios{cores.fimCor}')
valores = list(randint(1,100) for _ in range(5))
print(f'{valores}\n')

# Ajustando valores em ordem.
print(f'{cores.verde}# Ajustando valores em ordem.{cores.fimCor}')
valores.sort()
print(f'{valores}\n')

# Ajustando valores em ordem reversa.
print(f'{cores.verde}# Ajustando valores em ordem reversa.{cores.fimCor}')
valores.sort(reverse=True)
print(f'{valores}\n')

# Tamanho da lista.
print(f'{cores.verde}# Tamanho da lista.{cores.fimCor}')
print(f'{len(valores)}\n')

# Igualando listas cria uma ligação entre as duas listas.
print(f'{cores.verde}# Igualando listas.{cores.fimCor}')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Valor da lista A é {a}\nValor da lista B é {b}\n')

#-+---------+
# | AULA 18 |
#-+---------+

# Realizando uma cópia entre as listas
print(f'{cores.verde}# Realizando uma cópia entre as listas.{cores.fimCor}')
c = [3, 5, 6, 1]
d = c[:]
d[3] = 44
print(f'Os valores da list C são: {c}\nOs valores da lista D são {d}\n')

# Inserindo uma lista dentro de outra lista (Listas compostas)
dados = ["Pedro", 25]
pessoas = []

pessoas.append(dados[:]) # Importante que seja (dados[:]) e não somente (dados) pois apenas este, crie um elo entre as lista igual se fosse pessoas = dados

# 3 listas dentro de uma
pessoas = [["Pedro", 25],["Maria", 19],["João", 32]]

#-+------------------+------------------+-----------------+
# | +---------+----+ | +---------+----+ | +--------+----+ |
# | | 'Pedro' | 25 | | | 'Maria' | 19 | | | 'João' | 32 | |
# | +---------+----+ | +---------+----+ | +--------+----+ |
# |      0      1    |     0       1    |      0      1   |
#-+------------------+------------------+-----------------+
#         0                   1                 2

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])