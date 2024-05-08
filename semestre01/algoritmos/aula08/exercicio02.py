count = int(input('Quanto números serão digitados? '))
value = 0

for i in range(1, count + 1):
  value += int(input("Digite o " + str(i) + "º valor: "))

print("A média dos valores é: " + str(value / count))