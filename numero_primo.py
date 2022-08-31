'''
Dado um número fornecido pelo usuário, faça um programa que teste se é número primo
e imprima na tela. Além disso, exiba uma lista de divisores do número testado.
Um número primo é divisível somente por 1 e por ele mesmo. Seu programa deve ser funcional para qualquer número até o 100.

13 é divisível somente por 1 e ele mesmo (13), então é primo.
25 é divisível por 1, 5 e ele mesmo (25), então NÃO é primo.
'''

divisores = []
divisor = 0

seu_numero = int(input("Informe um número : "))

if seu_numero <= 100:
  for numero in range(2,seu_numero):
    if (seu_numero%numero == 0):
      divisores.append(numero)
      divisor += 1

  if (divisor == 0):
    print(f"{seu_numero} é divisível somente por 1 e ele mesmo ({seu_numero}), então é primo.")
  else:
    print(f"{seu_numero} por 1, {str(divisores).strip('[]')} e ele mesmo ({seu_numero}), então NÃO é primo.")
else:
  print("A entrada é inválida! Tente novamente.")


# Informe um número : 45
# 45 por 1, 3, 5, 9, 15 e ele mesmo (45), então NÃO é primo.

# Informe um número : 13
# 13 é divisível somente por 1 e ele mesmo (13), então é primo.


