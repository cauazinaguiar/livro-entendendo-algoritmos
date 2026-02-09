import math

usuario_caua = [5, 1, 2]
usuario_thales =[2, 2, 1]

def calcular_distancia(pessoa1, pessoa2):
    soma_quadrados = 0

    for i in range(len(pessoa1)):

        soma_quadrados += (pessoa1[1] - pessoa2[i]) ** 2

    return math.sqrt(soma_quadrados)

distancia = calcular_distancia(usuario_caua, usuario_thales)
print(f"A distância entre os perfis é: {distancia:.2f}")