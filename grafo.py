""" Discentes: Ana Gabriela Silva Barbosa e Elise Lissa Hasegawa"""

# -*- coding: utf-8 -*-
import random
from collections import deque

# Gera um grafo aleatório com n vértices e probabilidade p de conexão.
# Retorna o grafo como uma lista de adjacência.
def gerar_grafos(n, p):
    """
    Gera um grafo aleatório com `n` vértices e probabilidade `p` de conexão.
    Retorna o grafo como um dicionário de adjacência.
    """
    grafo = {}  #dicionário 
    for i in range(n):
        grafo[i] = []
    
    for i in range(n):
        for j in range(i + 1, n):  
            if random.random() < p:  
                grafo[i].append(j)
                grafo[j].append(i)  
    return grafo

# Calcula o grau mínimo, máximo e médio de um grafo representado como lista de adjacência.
def calcular_grau(grafo):
    
    graus = {vertice: len(vizinhos) for vertice, vizinhos in grafo.items()}
    gmin = min(graus.values())
    gmax = max(graus.values())
    gmed = sum(graus.values()) / len(graus)
    return gmin, gmax, gmed

def calcular_diametro(grafo):
    def bfs_distancia(grafo, inicio):
        # Realiza uma busca em largura (BFS) para calcular distâncias de inicio para todos os vértices.
        distancias = [-1] * len(grafo)
        fila = deque([inicio])
        distancias[inicio] = 0

        while fila:
            atual = fila.popleft()
            for vizinho in grafo[atual]:
                if distancias[vizinho] == -1:
                    distancias[vizinho] = distancias[atual] + 1
                    fila.append(vizinho)
        return distancias

    diametro = 0
    for v in range(len(grafo)):
        distancias = bfs_distancia(grafo, v)
        max_distancia = max(dist for dist in distancias if dist != -1)
        diametro = max(diametro, max_distancia)

    return diametro

# main
ini = int(input("ini: "))
fim = int(input("fim: "))
stp = int(input("stp: "))
p = float(input("p: "))

if not (0 < p <= 0.25):
    raise ValueError("A probabilidade p deve estar no intervalo 0 < p ≤ 0.25.")

print("V \tE \tgmin \tgmax \tgmed \tdiam")
print("---------------------------------------------")

for n in range(ini, fim + 1, stp):
    grafo = gerar_grafos(n, p)

    num_arestas = sum(len(vizinhos) for vizinhos in grafo.values()) // 2

    gmin, gmax, gmed = calcular_grau(grafo)
    diam = calcular_diametro(grafo)

    print(f"{n} \t{num_arestas} \t{gmin} \t{gmax} \t{gmed:.2f} \t{diam}")
