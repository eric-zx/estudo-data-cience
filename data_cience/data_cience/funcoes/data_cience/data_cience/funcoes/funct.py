import math


notas ={
    '1 trimestre': 8.5,
    '2 trimestre': 9.5,
    '3 trimestre':7.0
}
soma = 0
somatoria = sum(notas.values())

for nota in notas.values():
    #Para cada nota que existir dentro do conjunto de valores das notas, repita o código abaixo
    soma += nota
    

qtd_notas = len(notas)
print(qtd_notas)
print(somatoria )

media = somatoria / qtd_notas
print(media)
media = round(media)
print(round(media))





