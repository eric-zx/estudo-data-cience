# 1. Criamos uma lista vazia para armazenar o que você digitar
notas_usuario = []

# 2. Definimos quantas notas queremos pedir


for nota in range(3):
    # Pedimos a nota e convertemos para float
    valor = float(input(f"Digite a nota {nota+1}: "))
    notas_usuario.append(valor)

    # 3. Agora calculamos as globais com base no que foi digitado
    somatoria = sum(notas_usuario)
    qtd = len(notas_usuario)

# 4. Sua função (mantendo a lógica de parâmetros padrão)
def calcular_media(s = somatoria, q = qtd):
    resultado_media = s / q 
    print(f"Valor dentro da função (Local): {round(resultado_media)}")

# Execução
calcular_media()
print(f"Soma total acessada fora (Global): {round(somatoria)}")