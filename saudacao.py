# Faça uma função que recebe um nome e um horário
# e imprime “Bom dia, [nome]”, caso seja antes de 12h,
# “Boa Tarde, [nome]”, caso seja entre 12h e 18h e
# “Boa noite, [nome]” se for após às 18h.

from datetime import datetime

def saudacao(nome, horario):
  if horario < 12:
    print(f"Bom dia, {nome}")
  elif horario >= 12 and horario <= 18:
    print(f"Boa tarde, {nome}")
  elif horario > 18:
    print(f"Boa noite, {nome}")

seu_nome = input("Informe seu nome: ")
hora = datetime.now().hour
print(hora)
saudacao(seu_nome, hora)

