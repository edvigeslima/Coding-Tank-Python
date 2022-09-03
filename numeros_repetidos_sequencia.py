'''
Faça um script que leia 10 números do usuário e informe se algum número foi inserido em sequência.
Se mais de um número for repetido, informe ao menos um (caso no Exemplo 3).

Exemplo 1
input 1: 3
input 2: 5
(etc...) 6.. 7.. 12.. 2... 43.. 5.. 
input 9: 1
input 10: 8
output: Nenhum número foi repetido em sequência
Exemplo 2
input 1: 9
input 2: 4
(etc...) 9.. 5.. 9.. 6... 3.. 1.. 
input 9: 6
input 10: 6
output: O número 6 foi repetido em sequência
Exemplo 3
input 1: 2
input 2: 3
(etc...) 9.. 9.. 4.. 6... 7.. 7.. 
input 9: 4
input 10: 3
output: O número 7 foi repetido em sequência

'''
contador = 0
numeros = list()
repetido = list()

while (contador < 10):
  seu_numero = int(input(f"Digite o {contador+1}º número: "))
  numeros.append(seu_numero)
  contador += 1

print(numeros)

for n in range(len(numeros)-1):
  if numeros[n] == numeros[n+1]:
    repetido.append(numeros[n])

if len(repetido) != 0:
  print(f"O número {repetido} foi repetido em sequência.")
else:
  print("Nenhum número foi repetido em sequência.")
