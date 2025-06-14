# funcoes_estatisticas.py

import statistics as stats

def calcular_media(valores):
    return round(stats.mean(valores), 2)

def calcular_mediana(valores):
    return stats.median(valores)

def calcular_moda(valores):
    try:
        return stats.mode(valores)
    except stats.StatisticsError:
        return "Sem moda"

def calcular_variancia(valores):
    return round(stats.variance(valores), 2)

def calcular_desvio_padrao(valores):
    return round(stats.stdev(valores), 2)

def calcular_amplitude(valores):
    return max(valores) - min(valores)
