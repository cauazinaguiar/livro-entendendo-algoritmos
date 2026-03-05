# exercicio 3(algoritmos gulosos) : O Problema: "A Escala de Fotógrafo de Casamento" 
# Um fotógrafo recebeu vários pedidos de trabalho para o mesmo dia,
# mas cada trabalho começa e termina em horários diferentes. 
# Ele não pode estar em dois lugares ao mesmo tempo.
# A tarefa: Usar a lógica gulosa para escolher o maior
# número possível de eventos que ele consegue fotografar sem que os horários se sobreponham.

eventos = [
    ("Ensaio Gestante", 10.0, 11.5),
    ("Casamento Civil", 11.0, 12.5),
    ("Aniversário Infantil", 12.0, 14.0),
    ("Ensaio Pet", 13.5, 15.0),
    ("Formatura", 14.5, 16.5),
    ("Book de Moda", 16.0, 17.0)
]

eventos.sort(key=lambda x: x[2])

agenda = []
horario_fim_ultimo_evento = 0

for nome, inicio, fim in eventos:
    horario_inicio_evento = inicio
    if horario_inicio_evento >= horario_fim_ultimo_evento:
        agenda.append(nome)
        horario_fim_ultimo_evento = fim

print("Agenda do dia:", agenda)