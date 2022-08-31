'''
Super Desafio - Faça um programa que pede para o usuário digitar o CPF e verifica
se ele é válido. Para isso, primeiramente o programa deve multiplicar cada um dos
9 primeiros dígitos do CPF pelos números de 10 a 2 e somar todas as respostas.
O resultado deve ser multiplicado por 10 e dividido por 11. O resto dessa divisão
deve ser igual ao primeiro dígito verificador (10º dígito). Em seguida, o programa
deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e
repetir o procedimento anterior para verificar o segundo dígito verificador.

Exemplo:

Se o CPF for 286.255.878-87 o programa deve fazer primeiro:

x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)

O décimo número do CPF:
# Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
# Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
Se sim, o programa deve calcular:

x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)

O décimo primeiro número do CPF:
# Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
# Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
'''
valida_10 = False
valida_11 = False

num_CPF = input("Informe o CPF: ")
CPF = num_CPF.replace('.', '', 2).replace('-', '')
num_10 = 10
digito_10 = 0

for i in range(9):
  digito_10 += int(CPF[i])*num_10
  num_10 -= 1

# 10º dígito
# Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
# Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).

if (digito_10%11)<2 and int(CPF[9]) == 0:
  valida_10 = True
elif (digito_10%11)>=2 and int(CPF[9]) == 11-(digito_10%11):
  valida_10 = True


# 11 dígito
if valida_10 == True:
  num_11 = 11
  digito_11 = 0

  for i in range(10):
    digito_11 += int(CPF[i])*num_11
    num_11 -= 1
  
  if (digito_11%11)<2 and int(CPF[10]) == 0:
    valida_11 = True
  elif (digito_11%11)>=2 and int(CPF[10]) == 11-(digito_11%11):
    valida_11 = True


if (valida_10 == True and valida_11 == True):
  print(f"O CPF {num_CPF} é válido.")
else:
  print(f"O CPF {num_CPF} é inválido.")