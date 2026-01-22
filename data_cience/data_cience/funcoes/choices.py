from random import choices

pessoas = ['Eric', 'Ana', 'Bruce']
# Definindo pesos: Ana e Bruce têm 40% de chance cada, Eric só 20%
sorteio = choices(pessoas, weights=[1, 7.5, 7.5], k=2)

print(f"O sorteado foi: {sorteio}")