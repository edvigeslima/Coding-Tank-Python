'''
Um parque de diversões tem 3 atrações principais: o carrossel, piscina de bolinhas e montanha-russa.

Para poder participar de uma atração a pessoa deve cumprir as seguintes condições:

Carrossel: altura mínima de 1,00m e idade mínima de 3 anos.

Piscina de bolinhas: idade entre 4 e 9 anos e máximo de 1,30m de altura.

Montanha-russa: altura mínima de 1,10m.
O fiscal de cada atração verificará o ano de nascimento da pessoa e altura para liberar o acesso para uma pessoa.

Faça uma função em python que receba o ano de nascimento e altura da pessoa e informe quais as atrações que a pessoa pode participar.
'''

from datetime import datetime

def verificar_pessoa(ano_nascimento, altura_pessoa):

  idade = datetime.now().year - ano_nascimento
  carrossel = False
  piscina = False
  montanha_russa = False

  # Carrossel: altura mínima de 1,00m e idade mínima de 3 anos.
  if (altura_pessoa >= 1 and idade >= 3):
    carrossel = True
    print("\nCarrossel: acesso foi liberado.\n")
  else:
    print("\nCarrossel: acesso não foi liberado.\n")

  # Piscina de bolinhas: idade entre 4 e 9 anos e máximo de 1,30m de altura.
  if ((idade <= 9 and idade >= 4) and altura_pessoa <= 1.30):
    piscina = True
    print("Piscina de bolinhas: acesso foi liberado.\n")
  else:
    print("Piscina de bolinhas: acesso não foi liberado.\n")


  # Montanha-russa: altura mínima de 1,10m.
  if (altura_pessoa >= 1.10):
    montanha_russa = True
    print("Montanha-russa: acesso foi liberado.\n")
  else:
    print("Montanha-russa: acesso não foi liberado.\n")




seu_ano_nascimento = int(input("Digite seu ano de nascimento: "))
sua_altura = float(input("Digite sua altura: "))

verificar_pessoa(seu_ano_nascimento, sua_altura)
