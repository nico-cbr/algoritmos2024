# INSIRA
notaUm = float(input("Insira a 1ª nota: "))
notaD = float(input("Insira a 2ª nota: "))
notaT = float(input("Insira a 3ª nota: "))
notaQ = float(input("Insira a 4ª nota: "))

media = (notaUm + notaD + notaT + notaQ) / 4

print(f"A media é {media}")

if media < 60:
  print("O aluno está reprovado")
elif media < 80:
  print("O resultado foi bom")
elif media < 99:
  print("O resultado foi excelente!")
else:
  print("Sua nota foi maxíma, parabéns!!!")
