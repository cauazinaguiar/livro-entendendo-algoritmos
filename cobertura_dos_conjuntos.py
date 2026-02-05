estados_para_cobrir = set(["df","rj","sp","ce","rs","am","pr","es"])

estacoes = {}

estacoes["um"] = set(["ce","rs","am"])
estacoes["dois"] = set(["df","rj","ce"])
estacoes["tres"] = set(["sp","rs","pr"])
estacoes["quatro"] = set(["rs","am"])
estacoes["cinco"] = set(["pr","es"])

estacoes_final = set()

while estados_para_cobrir:
    melhor_estacao = None
    estados_cobertos = set()

    for estacao, estados_estacao in estacoes.items():
        cobertura = estados_para_cobrir & estados_estacao

        if len(cobertura) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertura
        
    estados_para_cobrir -= estados_cobertos
    estacoes_final.add(melhor_estacao)

print(estacoes_final)