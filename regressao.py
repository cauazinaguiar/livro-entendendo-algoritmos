import math 

historico_vendas = {
    "dia_1": {"caracteristicas": [5,1,0], "vendas": 300},
    "dia_2": {"caracteristicas": [3,1,1], "vendas": 225},
    "dia_3": {"caracteristicas": [1,0,0], "vendas": 75},
    "dia_4": {"caracteristicas": [4,0,1], "vendas": 200},
    "dia_5": {"caracteristicas": [4,1,0], "vendas": 250}
}

def calcular_distancia(lista1,lista2):
    soma = sum([(a-b) ** 2 for a, b in zip(lista1,lista2)])
    return math.sqrt(soma)

hoje = [4,1,0]

distancias = []

for dia in historico_vendas.values():
    d = calcular_distancia(hoje, dia["caracteristicas"])
    distancias.append((d, dia["vendas"]))

distancias.sort(key=lambda x: x[0])

k = 3

vizinhos_proximos = distancias[:k]
soma_vendas = sum([venda for dist, venda in vizinhos_proximos])
previsao = soma_vendas / k

print(f"Previsão de vendas: {int(previsao)} pães")