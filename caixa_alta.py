# Faça uma função que recebe uma lista de palavras e
# retorna uma lista contendo as mesmas palavras da lista anterior,
# porém escritas em caixa alta.

def caixa_lista (lista_palavras):
  nova_lista_palavras = []
  for palavra in lista_palavras:
    nova_lista_palavras.append(palavra.upper())
  return nova_lista_palavras

palavra = input("Insira os itens da lista: ")
palavras = palavra.split(" ")
print(caixa_lista(palavras))