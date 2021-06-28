estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')


'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Pailo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''

'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5'''
#del pessoas['Sexo']
#pessoas['nome'] = 'Leandro'
'''for k, v in pessoas.items():
    print(f'{k} = {v}')'''


#print(pessoas.items())
#print(pessoas.values())
#print(pessoas.keys())
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
