value = 0
i = 1

for i in range(1, 5):
  value += int(input("Digite o " + str(i) + "º valor: "))

print("O valor total é: " + str(value))