import matplotlib.pyplot as plt
import numpy as np


estudantes = ['Eric','Ana Julia','Bruce']
np.notas = [9.5 , 8.5 , 9.0]
novos_alunos = ['Carlos','Marcella']
notasNovas =[8, 7]
estudantes.append('Carol')
estudantes.extend(novos_alunos)
np.notas.append(10.0)
np.notas.extend(notasNovas)
print(estudantes)
print(np.notas)

plt.bar(x = estudantes, height=  np.notas)
plt.show()
