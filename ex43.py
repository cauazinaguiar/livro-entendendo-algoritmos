def maior(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_maximo = maior(lista[1:])
    return lista[0]  if lista[0] > sub_maximo else sub_maximo

print (maior([2,5,1,8,4]))