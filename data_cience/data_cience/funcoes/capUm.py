import matplotlib.pyplot as plt
import numpy as np
from random import choices
help(choices)
estudantes = ['Eric','Ana Julia','Bruce']
np  = notas = [9.5 , 8.5 , 9.0]
novos_alunos = ['Carlos','Marcella']
notasNovas =[8, 7]
estudantes.append('Carol')
estudantes.extend(novos_alunos)
notas.append(10.0)
notas.extend(notasNovas)
print(estudantes)
print(notas)

plt.bar(x = estudantes, height=  notas)
plt.show()

