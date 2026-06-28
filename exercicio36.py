# 036 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valo da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
hauseValue = float(input("Valor da casa: "))
salary = float(input("Salário do comprador: "))
years = int(input("Anos para serem pagos: "))
monthlyValue = hauseValue/years

# print(monthlyValue)
# print((salary*30)/100)

if monthlyValue > (salary*30)/100:
    print("\033[0;31mNegado!\033[m O valor da prestação excede 30% do salário. ")
else:
    print(f"Valor mensal à ser pago R${hauseValue/years:.2f} por {years} anos.")