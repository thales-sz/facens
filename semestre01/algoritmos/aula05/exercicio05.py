number = int(input("Digite um número de 3 digitos: "))

if number < 100 or number > 999:
    print("O número deve ter 3 digitos")
else:
    first_digit = number // 100
    second_digit = (number % 100) // 10
    third_digit = number % 10

    print(first_digit, second_digit, third_digit)
