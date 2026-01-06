def contador(lista):
    if lista == []:
        return 0
    return 1 + contador(lista[1:])

print (contador([2,4,6,1]))