cand01 = 0
cand02 = 0
cand03 = 0
branco = 0
nulo = 0

print('Candidato 01 - Digite 1\n'
      'Candidato 02 - Digite 2\n'
      'Candidato 03 - Digite 3')

while((cand01 + cand02 + cand03 + nulo + branco) < 10):

  voto = int(input("Qual o candidato que você votará? "))

  match voto:
    case 1:
      print('Voto confirmado para Candidato 01')
      cand01 += 1
    case 2:
      print('Voto confirmado para Candidato 02')
      cand02 += 1
    case 3:
      print('Voto confirmado para Candidato 03')
      cand03 += 1
    case 4:
      print('Voto em branco')
      branco += 1
    case _:
      print("Voto nulo")
      nulo += 1

print('Candidato 01: ', cand01)
print('Candidato 02: ', cand02)
print('Candidato 03: ', cand03)
print('Votos em branco: ', branco)
print('Votos nulos: ', nulo)
print('Votos válidos: ', cand01 + cand02 + cand03 + branco)

if cand01 > cand02 and cand01 > cand03:
  print('Vencedor da votação é: Candidato 01. Com', cand01, 'votos')
elif cand02 > cand01 and cand02 > cand03:
  print('Vencedor da votação é: Candidato 02. Com', cand02, 'votos')
else:
  print('Vencedor da votação é: Candidato 03. Com', cand03, 'votos')
