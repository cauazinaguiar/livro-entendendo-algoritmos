from collections import deque

grafo ={}
grafo["voce"] = ["yuri", "ze", "maria"]
grafo["yuri"] = ["paulo", "anthony"]
grafo["ze"] = ["adriana", "laura"]
grafo["maria"] = ["laura"]
grafo["paulo"] = []
grafo["anthony"] = []
grafo["adriana"] = []
grafo["laura"] = []

def e_vendedor(nome):
    return nome[-1] == 'y'

def grafovendedor(nome):
    fila_pessoa = deque()
    fila_pessoa += grafo[nome]
    verificadas = []
    while fila_pessoa:
        pessoa = fila_pessoa.popleft()
        if not pessoa in verificadas:
            if e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor")
                return True
            else:
                fila_pessoa +=grafo[pessoa]
                verificadas.append(pessoa)
    print("Ninguém é vendedor")
    return False

grafovendedor("voce")