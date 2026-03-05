# exercicio 5(knn e regressão) : O Problema: "Previsão de Preço de Carro Usado" 
# Baseado no ano do carro, na quilometragem e na conservação, 
# você quer prever por quanto deve vender o seu carro.

# A tarefa: Usar o histórico de preços de carros parecidos para calcular,
# via distância euclidiana e média, o preço justo do seu.

import math

# Características: [Ano (de 0 a 10, onde 10 é novo), KM (em milhares), Conservação (1 a 5)]
historico_carros = [
    {"caracteristicas": [10, 5, 5], "preco": 50000}, # Carro quase novo
    {"caracteristicas": [8, 20, 4], "preco": 40000},
    {"caracteristicas": [5, 50, 3], "preco": 25000},
    {"caracteristicas": [2, 100, 1], "preco": 10000}  # Carro bem usado
]

meu_carro = [9, 10, 5] # Ano 9, 10 mil KM, Conservação 5

def calc_distancia(lista1, lista2):
    soma = 0
    for i in range(len(lista1)):
        soma += (lista1[i] - lista2[i]) ** 2
    return math.sqrt(soma)


def prever_preco(historico, carro_alvo, k=2):
    distancias = []

    for carro in historico:
        d = calc_distancia(carro["caracteristicas"], carro_alvo)
        distancias.append((d, carro["preco"]))
    
    distancias.sort(key =lambda x: x[0])

    vizinhos = distancias[:k]
    
    media = sum(preco for _, preco in vizinhos) / k
    return media, vizinhos

preco_previsto, vizinhos = prever_preco(historico_carros,meu_carro, k=2)

print("Vizinhos mais próximos:", vizinhos)
print(f"Preço previsto: R$ {preco_previsto:,.2f}")

