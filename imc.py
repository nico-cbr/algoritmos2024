# 1 crie um algoritmo que calcule o imc de uma pessoa, as entradas são peso e altura
# imc = peso / altura^2

peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / (altura * altura)

print(f"O seu imc é {imc}")