# 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str('Ana Maria de Souza').strip().title()
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print(f'Primeiro nome: {primeiro_nome}\nÚltimo nome: {ultimo_nome}')