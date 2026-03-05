# exercicio 2(dijkstra) : O Problema: "A Rota de Entrega Mais Barata"
# Você tem um caminhão de entregas e várias rotas possíveis entre cidades.
# Cada rota tem um custo de pedágio/combustível diferente.

# A tarefa: Calcular a rota que gaste o menor valor de dinheiro para ir
# da "Sede da Empresa" até o "Cliente Final", passando por cidades intermediárias.

grafo = {}

grafo["Sede"] = {"Cid_A": 5, "Cid_B": 2}
grafo["Cid_A"] = {"Cid_C": 4, "Cid_D": 2}
grafo["Cid_B"] = {"Cid_A": 8, "Cid_D": 7}
grafo["Cid_C"] = {"Cliente": 3, "Cid_D": 6}
grafo["Cid_D"] = {"Cliente": 1}
grafo["Cliente"] = {}

infinito = float("inf")
custos = {"Cid_A": 5, "Cid_B": 2, "Cid_C": infinito, "Cid_D": infinito, "Cliente": infinito}

pais = {"Cid_A": "Sede", "Cid_B": "Sede", "Cid_C": None, "Cid_D": None, "Cliente": None}

processados = []

def achar_mais_barato(custos):
    custo_mais_baixo = float("inf")
    node_custo_mais_baixo = None

    for no in custos: 
        custo = custos[no]
        if custo < custo_mais_baixo and no not in processados:
            custo_mais_baixo = custo
            node_custo_mais_baixo = no
    return node_custo_mais_baixo
    
no = achar_mais_barato(custos)

while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = achar_mais_barato(custos)

print(f"Curso total: {custos['Cliente']}")

caminho = ["Cliente"]
pai_atual = pais["Cliente"]

while pai_atual is not None:
    caminho.append(pai_atual)
    pai_atual = pais.get(pai_atual)

caminho.reverse()
print("A rota mais barata da sede para o cliente é:", "->".join(caminho))