"""""
Em uma eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""

quant_eleitores = int(input('Informe a quantidade de eleitores: '))

candidatos = {'candidato_1': 0, 'candidato_2': 0, 'candidato_3': 0}

for quant_eleitores in range (1, quant_eleitores+1):

    votos = int(input(f'Eleitor número {quant_eleitores}. Digite seu voto: '))

    if votos == 1:
        candidatos['candidato_1'] += 1
    elif votos == 2:
        candidatos['candidato_2'] += 1
    else:
        candidatos['candidato_3]'] +=1

print(f"Primeiro candidato: {candidatos['candidato_1']} votos. Segundo candidato: {candidatos['candidato_2']} votos. Terceiro candidato: {candidatos['candidato_3']} votos")

