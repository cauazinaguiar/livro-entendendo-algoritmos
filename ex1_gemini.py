# exercicio 1(grafo e bfs) : O Problema: "Conexão de LinkedIn"
# Crie um algoritmo que verifique se você está conectado a uma pessoa específica
# (ex: um recrutador) através de sua rede de contatos.
# A tarefa: Você tem um grafo de amigos.
# Deve encontrar se o "Recrutador" está na sua rede e a quantos "pulos" ele está de você.

from collections import deque

grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
grafo["alice"] = ["anuj", "peggy"]
grafo["bob"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = ["recrutador"] 
grafo["jonny"] = []
grafo["recrutador"] = []

def e_recrutador(nome):
    return nome == "recrutador"

def pesquisa_recrutador(nome):
    fila_pessoa = deque()

    for amigo in grafo[nome]:
        fila_pessoa.append([amigo, 1])

    verificados = []

    while fila_pessoa:
        pessoa, distancia = fila_pessoa.popleft()

        if not pessoa in verificados:
            if e_recrutador(pessoa):
                print(f"Recrutador encontrado na sua rede de amigos. Ele é um amigo de {distancia}º grau")
                return True
            else:
                for vizinho in  grafo[pessoa]:
                    fila_pessoa.append([vizinho, distancia + 1]) 
                verificados.append(pessoa)
    print("Infelizmente não tem recrutador na sua lista de amigos")
    return False

pesquisa_recrutador("voce")