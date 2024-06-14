import random

# numAleatorio = random.randint(1, 100);
# print(f"seu numero é {numAleatorio}, recarregue pra conseguir outro");

def sortear(minimo, maximo):
  return random.randint(minimo, maximo)

minimo = 1
maximo = 10
# print( sortear(minimo, maximo))
sorteado = sortear(minimo, maximo)

num = int(input("insira qualquer número: "))

while True:
  if num > 10 or num < 0:
    print("O numero tem que ser entre 1 e 10")
    num = int(input("Insira qualquer numero: "))
  

  if sorteado < num:
    print("O número secreto é menor")
    num = int(input("Insira qualquer numero: "))
  elif sorteado > num:
    print("O número secreto é maior ")
    num = int(input("Insira qualquer numero: "))
  elif sorteado == num:
    print(f"você acertou o numero é {sorteado}")
    break
  