votou = {}

def verificacao(nome): #usando tabela hash
    if votou.get(nome):
        print("Mande embora")
    else:
        votou[nome] = True
        print("Deixe votar")

verificacao("Tom")
verificacao("Caua")
verificacao("Tom")
verificacao("Caua")
verificacao("Jorge")