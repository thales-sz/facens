# Ano bissexto -> Deve ser multiplo de 4 mas não pode ser multiplo de 100 a menos que seja multiplo de 400

year = int(input("Digite um ano para saber se ele é bissexto: "))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
  print(year, "é um ano bissexto")
else:
  print(year, "não é um ano bissexto")