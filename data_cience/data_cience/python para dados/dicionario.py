lista_clientes = []

# Em vez de contador, usamos uma variável de controle
continuar = '1'

while continuar == '1':
    nome = input('Digite seu nome: ') 
    cpf = input('Digite seu CPF: ')   
    idade = int(input('Digite sua idade: ')) 
    cnpj = input('Digite o cnpj de sua empresa: ')
    cep = input('Digite o cep de sua moradia: ')
    renda = int(input('Digite a renda anual: '))

    cliente = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'empresa': {
            'cnpj': cnpj,
            'cep': cep,
            'renda': renda
        }
    }

    lista_clientes.append(cliente)
    
    # Aqui perguntamos se o usuário quer cadastrar mais alguém
    continuar = input('\nDeseja cadastrar outro cliente? (1 para Sim, qualquer outra tecla para Sair): ')

# Agora o print final mostrará TODOS os cadastrados nesta sessão
print('\n--- Relatório de Todos os Clientes ---')
for c in lista_clientes:
    print(f"Nome: {c['nome']} | Empresa: {c['empresa']['cnpj']}")
#keys

for chaves in cliente.keys():
    print(cliente[chaves])

#values

    print(cliente.values())
# Resultado: dict_values(['Eric', '123.456.789-00', 25])

# Exemplo prático:
for valor in cliente.values():
    print(f"Valor guardado: {valor}")

for chave, valor in cliente.items():
    print(f"{chave.upper()}: {valor}")

# Resultado:
# NOME: Eric
# CPF: 123.456.789-00
# IDADE: 25