# main.py

from funcoes_estatisticas import (
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_variancia,
    calcular_desvio_padrao,
    calcular_amplitude
)

# Dados dos produtos
produtos = {
    "Iphone": [4000, 5600, 12000],
    "Fone": [50, 250, 400],
    "Carregador": [70, 150, 300],
    "Capinha": [25, 40, 50],
    "Pelicula": [25, 30, 35],
    "Mouse": [62, 72, 92],
    "Tenis": [700, 1000, 13000],
    "Moletom": [90, 150, 350],
    "Calça": [100, 130, 160],
    "Camiseta": [55, 75, 85]
}

# Executa estatísticas para todos os produtos
for produto, valores in produtos.items():
    print(f"\n📦 Produto: {produto}")
    print(f"  Média: {calcular_media(valores)}")
    print(f"  Mediana: {calcular_mediana(valores)}")
    print(f"  Moda: {calcular_moda(valores)}")
    print(f"  Variância: {calcular_variancia(valores)}")
    print(f"  Desvio Padrão: {calcular_desvio_padrao(valores)}")
    print(f"  Amplitude: {calcular_amplitude(valores)}")
