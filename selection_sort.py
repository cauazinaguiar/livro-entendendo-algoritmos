def buscaMenor (arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao (arr):
    copiaArr = list(arr)
    novoArr = []
    for i in range(len(copiaArr)):
        indice_menor = buscaMenor(copiaArr)
        novoArr.append(copiaArr.pop(indice_menor))
    return novoArr

minha_lista = [5, 3, 6, 2, 10]
lista_ordenada = ordenacaoporSelecao(minha_lista)

print (f"Original: {minha_lista}")
print (f"Ordenada: {lista_ordenada}")