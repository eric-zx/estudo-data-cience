carros_vendidos =['corsa','onix','HRV-Honda','corsa','onix','HRV-Honda']
print(carros_vendidos)

print(set[str](carros_vendidos))


#dicionarios /= de listas

#dicionarios:
print('\nCRIANDO DICIONÁRIO...')
carros = {
'nome': input('Digite o nome do veículo: '),
'ano': int(input('Digite o ano do veículo: ')),
'valor':float(input('Digite o valor do veículo: '))
}

print(carros)