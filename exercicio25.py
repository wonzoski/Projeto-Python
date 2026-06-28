# 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = 'Fabrício Wonzoski silva'
nome = nome.strip().title()

if 'Silva' in nome:
    print('Tem Silva no nome')
else:
    print('Não tem Silva no nome')