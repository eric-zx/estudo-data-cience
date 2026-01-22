# Lista para armazenar todos os alunos
lista_alunos = []

contador = 1
while contador <= 3:
    nome_aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))

    media = (nota1 + nota2 + nota3) / 3

    status = input('Fez o trabalho bimestral? (Digite 1 para Sim, 0 para Não): ')

    if status == '1':
        nota_trabalho = float(input('Digite a nota do trabalho: '))
        media = (media + (nota_trabalho/2))
        print('Nota do trabalho adicionada!')

    # Definindo o resultado com base na média
    if media >= 6:
        resultado = 'Aprovado'
    elif media >= 2.5:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'

    # Guardando os dados em um dicionário e adicionando à lista
    aluno = {
        'nome': nome_aluno,
        'media': media,
        'resultado': resultado
    }
    lista_alunos.append(aluno)

    print(f'A média final do(a) aluno {nome_aluno} foi: {media:.2f}')
    print(f'Status: {resultado}')
    print('-' * 20)
    
    contador += 1

# Exibindo a lista completa ao final
print('\n--- Relatório Final ---')
for aluno in lista_alunos:
    print(f"Nome: {aluno['nome']} | Média: {aluno['media']:.2f} | Status: {aluno['resultado']}")
    print(lista_alunos)