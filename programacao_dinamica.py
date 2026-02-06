itens = [
    {"nome": "violao", "valor": 1500, "peso": 1},
    {"nome": "radio", "valor": 3000, "peso": 4},
    {"nome": "notebook", "valor": 2000, "peso": 3},
    {"nome": "ihpone", "valor": 2000, "peso": 1}
]

capacidade_mochila = 4

matriz = [[0 for x in range(capacidade_mochila + 1)] for y in range(len(itens))]

for i in range(len(itens)):
    for j in range(1, capacidade_mochila + 1):
        valor_atual = itens[i]["valor"]
        peso_atual = itens[i]["peso"]

        if peso_atual <= j:
            valor_anterior = matriz[i-1][j] if i > 0 else 0

            espaco_restante = j - peso_atual
            valor_com_item = valor_atual + (matriz[i-1][espaco_restante] if i > 0 else 0)

            matriz[i][j] = max(valor_anterior, valor_com_item)
        else:
            matriz[i][j] = matriz[i-1][j] if i > 0 else 0

print (f"O valor máximo que a mochila pode carregar é: {matriz[-1][-1]}")