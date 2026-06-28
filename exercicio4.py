# 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informções possíveis sobre ela.
objeto = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(objeto).__name__}")
print(f"Só tem espaços? {objeto.isspace()}")
print(f"É um número? {objeto.isnumeric()}")
print(f"É alfabético? {objeto.isalpha()}")
print(f"É alfanumérico? {objeto.isalnum()}")
print(f"Está em maiúculas? {objeto.isupper()}")
print(f"Está em minúsculas? {objeto.islower()}")