# 083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

import cores

lista_expressão = list(str(input('Digite a expressão: ')))

# (())()()

while '(' in lista_expressão and ')' in lista_expressão and lista_expressão.index(')') > lista_expressão.index('('):
    lista_expressão.pop(lista_expressão.index('('))
    lista_expressão.pop(lista_expressão.index(')'))
    print(lista_expressão)
    
if '(' in lista_expressão or ')' in lista_expressão:
    print('Expressão inválida!')
else:
    print('Expressão válida.')