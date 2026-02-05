grafo = {}

grafo["inicio"] = {"a": 6, "b": 2}
grafo["a"] = {"fim": 1}
grafo["b"] = {"fim": 5, "a": 3}
grafo["fim"] = {}

print (grafo["inicio"].keys())
print (grafo["inicio"]["a"])
print (grafo["inicio"]["b"])

infinito = float("inf")

custos = {}

custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}

pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def dijkstra(custos):
    custo_mais_baixo = float("inf")
    no_custo_mais_baixo = None
    for no in custos: 
        custo = custos[no]
        if custo < custo_mais_baixo and no not in processados:
            custo_mais_baixo = custo
            no_custo_mais_baixo = no
    return no_custo_mais_baixo

no = dijkstra(custos)

while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = dijkstra(custos)

caminho = ["fim"]
pai_atual = pais["fim"]

while pai_atual is not None:
    caminho.append(pai_atual)
    pai_atual = pais.get(pai_atual)

caminho.reverse() 
print(" -> ".join(caminho))

print(f"Custo final para chegar ao fim é:{custos['fim']}")
