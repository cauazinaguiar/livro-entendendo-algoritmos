# exercicio 4(programação dinâmica) : O Problema: "Otimização de Espaço em Disco" 
# Você tem um HD externo com apenas 10GB livres e quer salvar filmes nele. 
# Cada filme tem um tamanho (GB) e uma nota (importância para você).

# A tarefa: Criar a grade para decidir quais filmes salvar 
# para ter o máximo de "nota/satisfação" total sem estourar os 10GB.

filmes = [
    {"nome": "Matrix", "tamanho": 1, "nota": 7},
    {"nome": "Interstellar", "tamanho": 4, "nota": 9},
    {"nome": "Inception", "tamanho": 3, "nota": 8},
    {"nome": "Avatar", "tamanho": 1, "nota": 6}
]
capacidade_hd = 4

matriz = [[0 for x in range(capacidade_hd + 1)] for y in range(len(filmes))]

for i in range(len(filmes)):
    for j in  range(1, capacidade_hd + 1):
        tamanho_atual = filmes[i]["tamanho"]
        nota_atual = filmes[i]["nota"]

        if tamanho_atual <= j:
            nota_anterior = matriz[i-1][j] if i > 0 else 0

            espaco_restante = j - tamanho_atual
            nota_com_filme = nota_atual + (matriz[i-1][espaco_restante] if i > 0 else 0 )

            matriz[i][j] = max(nota_anterior, nota_com_filme)
        else: 
            matriz[i][j] = matriz[i-1][j] if i > 0 else 0

print (f"O tamanho máximo de filmes que a mochila pode carregar é: {matriz[-1][-1]}")