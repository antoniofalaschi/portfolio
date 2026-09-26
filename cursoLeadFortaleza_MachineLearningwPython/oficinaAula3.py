#etapa 1

import numpy as np

visualizacao_stories = np.array([
[187, 120, 88, 70, 130, 168, 213],
[0, 0, 42, 0, 0, 55, 77],
[91, 0, 61, 0, 71, 121, 271],
[0, 0, 0, 0, 187, 0, 0],
[42, 23, 34, 0, 39, 29, 36]
])
pessoas = np.array(['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson'])
dias_semana = np.array(['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'])

print(visualizacao_stories.shape)

raquelDom = visualizacao_stories[0, :]


print('Média de visualizações por dia:')
for i in range(len(pessoas)):
    print(pessoas[i] + ' -> ' + str(visualizacao_stories[i, :].mean()))

print('\nDia de maior número de vusualizações de stories somadas:')
print(dias_semana[visualizacao_stories.sum(axis=0).argmax()], ' com ', visualizacao_stories.sum(axis=0)[visualizacao_stories.sum(axis=0).argmax()], ' visualizações.')

print('\nQuem foi que teve o maior número de visualizações na última semana?')
max_pessoa = visualizacao_stories.sum(axis=1).argmax()
print(pessoas[max_pessoa], 'que teve o maior número total, somando ', visualizacao_stories.sum(axis=1)[max_pessoa], ' visualizações.')


###################################################################

#etapa 2

import numpy as np
import numpy.ma as ma

visualizacao_stories = np.array([
[52, 68, 97, 55, -1, 98, -1],
[53, -1, 38, -1, -1, 72, 49],
[88, -1, 64, -1, 77, 130, 43],
[-1, 30, -1, -1, -1, 182, -1],
[41, 20, 33, -1, 37, 23, 7]
])
pessoas = np.array(['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson'])
dias_semana = np.array(['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'])

visualizacao_stories = np.ma.masked_where(visualizacao_stories  < 0, visualizacao_stories)

print(visualizacao_stories.shape)

raquelDom = visualizacao_stories[0, :]


print('Média de visualizações por dia:')
for i in range(len(pessoas)):
    print(pessoas[i] + ' -> ' + str(visualizacao_stories[i, :].mean()))

print('\nDia de maior número de vusualizações de stories somadas:')
print(dias_semana[visualizacao_stories.sum(axis=0).argmax()], ' com ', visualizacao_stories.sum(axis=0)[visualizacao_stories.sum(axis=0).argmax()], ' visualizações.')

print('\nQuem foi que teve o maior número de visualizações na última semana?')
max_pessoa = visualizacao_stories.sum(axis=1).argmax()
print(pessoas[max_pessoa], 'que teve o maior número total, somando ', visualizacao_stories.sum(axis=1)[max_pessoa], ' visualizações.')