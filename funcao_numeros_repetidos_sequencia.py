'''
Faça uma função que informe se algum número foi inserido em sequência.
Se mais de um número for repetido, informe ao menos um (caso no Exemplo 3).
O usuário digita 10 números.


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

def N_repeticoes (vetor):
    repetido = list()

    for n in range(len(vetor)-1):
        if vetor[n] == vetor[n+1] and vetor[n] not in repetido:
            repetido.append(vetor[n])

    return repetido

contador = 0
numeros = list()

while (contador < 10):
    seu_numero = int(input(f"Digite o {contador+1}º número: "))
    numeros.append(seu_numero)
    contador += 1


repeticao = N_repeticoes(numeros)
print(repeticao)
if len(repeticao) == 1:
  print(f"O número {repeticao} foi repetido em sequência.")
elif len(repeticao) > 1:
  print(f"Os números {str(repeticao).strip('[]')} foram repetidos em sequência.")
else:
  print("Nenhum número foi repetido em sequência.")