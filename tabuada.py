# Escreva um algoritmo que recebe um valor
# e imprima a sua tabuada

def tabuada (num):
    t = list()
    mult = 0
    n = 1
    t_tabuada = ""

    while n <= 10:
        mult = num * n
        t.append(mult)
        t_tabuada += f"Número {n} = {mult}\n"
        n += 1
    
    print(f"\n***** TABUADA {num} *****")
    print(t_tabuada)
 
numero = int(input("Digite um número: "))
tabuada(numero)

