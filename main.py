import numpy as np
from ocho_puzzle import MatrizOchoRompeCabezas
from dfs_Algoritmo import dfs_resolver
from bfs_Algoritmo import bfs_resolver


p = MatrizOchoRompeCabezas()

print("=== ESTADO INICIAL ===")
print(p.matriz)

meta = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])

print("\n=== ELIGE ALGORITMO ===")
print("1. Profundidad (DFS)")
print("2. Amplitud (BFS)")
opcion = input("Opcion: ")

print("\n=== RESULTADO ===")
if opcion == "1":
    dfs_resolver(p, meta, max_profundidad=30)
elif opcion == "2":
    bfs_resolver(p, meta)
else:
    print("Opcion no valida.")