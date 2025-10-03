from ocho_puzzle import MatrizOchoRompeCabezas
from dfs_Algoritmo import dfs_resolver
import numpy as np

p = MatrizOchoRompeCabezas()

meta = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,0]])

dfs_resolver(p, meta, max_profundidad=30)
