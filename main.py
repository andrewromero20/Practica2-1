import numpy as np
import time
from ocho_puzzle import MatrizOchoRompeCabezas
from dfs_Algoritmo import dfs_resolver
from bfs_Algoritmo import bfs_resolver


p = MatrizOchoRompeCabezas()

print("=== ESTADO INICIAL ===")
print(p.matriz)

meta = np.array([[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]])

print("\n=== ELIGE ALGORITMO ===")
print("1. Profundidad (DFS)")
print("2. Amplitud (BFS)")
opcion = input("Opcion: ")

print("\n=== RESULTADO ===")
if opcion == "1":
    inicio = time.perf_counter()
    dfs_resolver(p, meta, max_profundidad=30)
    fin = time.perf_counter()
    print("Tiempo de ejecucion DFS: " + str(fin-inicio))
elif opcion == "2":
    inicio = time.perf_counter()
    bfs_resolver(p, meta)
    fin = time.perf_counter()
    print("Tiempo de ejecucion BFS: " + str(fin - inicio))
else:
    print("Opcion no valida.")