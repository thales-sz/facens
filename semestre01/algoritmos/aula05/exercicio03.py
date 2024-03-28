height = float(input("Digite sua altura: "))

imc_man = (72.7 * height) - 58

imc_woman = (62.1 * height) - 44.7

print("O peso ideal para mulheres de", height, "de altura é:", imc_woman, "Kg")
print("O peso ideal para homens de", height, "de altura é:", imc_man, "Kg")