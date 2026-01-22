notas = [8.5, 7.5, 5.5]
somatoria = sum(notas)
qtd = len(notas)

def calcular_media(s = somatoria, q = qtd):
    resultado_media = s / q 
    print(f"Valor dentro da função (Local): {round(resultado_media)}")


calcular_media()


print(f"Soma total acessada fora (Global): {somatoria}")

