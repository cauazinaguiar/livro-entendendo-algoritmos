nome_a = "fish"
nome_b = "hish"

matriz = [[0 for x in range(len(nome_b))]for y in range(len(nome_a))]

for i in range(len(nome_a)):
    for j in range(len(nome_b)):
        if nome_a[i] == nome_b[j]:
            if i > 0 and j > 0:
                matriz[i][j] = matriz[i-1][j-1] + 1
            else: 
                matriz[i][j] = 1
        else: 
            matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])

print(f"O número de letras em comum é: {matriz[-1][-1]}")