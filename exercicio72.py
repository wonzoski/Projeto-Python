# 072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
import cores

unidades = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
)
valor = int(input('Digite um valor de 0 até 20: '))
while valor > 20:
    valor = int(input('Tente novamente! Digite um valor de 0 até 20: '))
print(unidades[valor])