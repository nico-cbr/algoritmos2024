# Gasolina = R$5,49
# Alcool = R$3,69

print("Olá mundo!")

# entrada
precoAlcool = float(input("Insira o valor do alcool: "))
precoGasolina = float(input("Insira o valor da gasolina: "))

# processamento
resultado = precoAlcool / precoGasolina

# saida 1
print(resultado)

# se o resultado for maior que 0.7 abastece gasolina, caso contrario, com alcool
if resultado > 0.7:
  print("Abasteça com gasolina!")
else:
  print("Abasteça com alcool!")