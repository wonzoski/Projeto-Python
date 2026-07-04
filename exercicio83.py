# 083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

import cores

lista_expressão = list(str(input('Digite a expressão: ')))

# Detectar o parenteses
#print(lista_expressão.count('('), lista_expressão.count(')'))

# ())()(

for x in range(len(lista_expressão)):
    if lista_expressão[x] == '(':
        for y in range(len(lista_expressão) - 1, -1, -1):
            if lista_expressão[y] == '(':
                print('A expressão não está correta.')
                break
            elif lista_expressão[y] == ')':
                lista_expressão.pop(x)
                lista_expressão.pop(y)