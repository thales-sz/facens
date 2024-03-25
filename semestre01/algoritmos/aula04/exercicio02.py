# Um aluno é aprovado quando sua média é maior do que 7.
# Escreva um programa que leia duas notas de um aluno e imprima se ele foi aprovado ou não.

grade1 = int(input("Digite a primeira nota: "))
grade2 = int(input("Digite a segunda nota: "))

aproved = (grade1 + grade2) / 2 >= 7

print("Aluno aprovado?", aproved)