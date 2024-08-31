for i in range(1, 6):
  print(i)



def media_vendas(vendas):
  soma = sum(vendas)
  tamanho = len(vendas)
  media = soma / tamanho
  return media

vendas = [[1000, 2000, 3000], [1500, 2500, 3500], [2000, 3000, 4000]]

* chamada da função