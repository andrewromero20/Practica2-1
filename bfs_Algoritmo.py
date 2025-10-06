import numpy as np
from copy import deepcopy
from collections import deque
from ocho_puzzle import MatrizOchoRompeCabezas

def bfs_resolver(puzzle, meta):
    objetivo = tuple(meta.flatten())
    estado_inicial = tuple(puzzle.matriz.flatten())

    
    queue = deque([(estado_inicial, puzzle.posicionVacia, [])])
    visitados = set()

    while queue:
        estado_tupla, posVacia, caminoRecorrido = queue.popleft()

        if estado_tupla in visitados:
            continue
        visitados.add(estado_tupla)

        
        if estado_tupla == objetivo:
            print("¡Solución encontrada con BFS!")
            for paso, est in enumerate(caminoRecorrido + [estado_tupla]):
                print(f"\nPaso {paso}:")
                print(np.array(est).reshape(3, 3))
            return True

        
        puzzle_actual = MatrizOchoRompeCabezas()
        puzzle_actual.matriz = np.array(estado_tupla).reshape(3, 3)
        puzzle_actual.posicionVacia = posVacia

        
        movimientos = []
        if puzzle_actual.se_puede_mover_arriba():
            hijo = deepcopy(puzzle_actual)
            hijo.mover_arriba()
            movimientos.append((tuple(hijo.matriz.flatten()), hijo.posicionVacia))

        if puzzle_actual.se_puede_mover_abajo():
            hijo = deepcopy(puzzle_actual)
            hijo.mover_abajo()
            movimientos.append((tuple(hijo.matriz.flatten()), hijo.posicionVacia))

        if puzzle_actual.se_puede_mover_izquierda():
            hijo = deepcopy(puzzle_actual)
            hijo.mover_izquierda()
            movimientos.append((tuple(hijo.matriz.flatten()), hijo.posicionVacia))

        if puzzle_actual.se_puede_mover_derecha():
            hijo = deepcopy(puzzle_actual)
            hijo.mover_derecha()
            movimientos.append((tuple(hijo.matriz.flatten()), hijo.posicionVacia))

        
        for nuevo_estado, nueva_pos in movimientos:
            queue.append((nuevo_estado, nueva_pos, caminoRecorrido + [estado_tupla]))

    print("No se encontró solución.")
    return False