'''
Peça ao usuário para entrar com um número e faça uma função que retorne
o fatorial dele como resposta. O fatorial de um número é o resultado da
multiplicação de todos os números que o antecedem a partir de 1 até o número fornecido.

Exemplo: fatorial de 4 = 1 * 2 * 3 * 4 = 24
'''

def fatorial(numero):
  produto = 1
  if numero == 0:
    return produto
  else:
  # n! = n * (n-1) * ... * 1
    for num in range(1, numero+1):
      produto *= num
    return produto


seu_numero = int(input("Informe um número : "))
if seu_numero >= 0:
  fatorial = fatorial(seu_numero)
  print(f"Fatorial de {seu_numero} = {fatorial}")
else:
  print("A entrada é inválida! Tente novamente.")
