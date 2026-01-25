import math as m

# Variável definida no escopo principal
notas = [8.5, 7.5, 5.5]

def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# Corrigindo o nome da variável para coincidir com o print
resultado = calcular_media(notas)

print(f'A média do aluno Eric foi de: {round(resultado)}')