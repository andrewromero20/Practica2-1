import numpy as np
from copy import deepcopy
from ocho_puzzle import MatrizOchoRompeCabezas
def dfs_resolver(puzzle, meta, max_profundidad=30):

    #estado de solucion
    objetivo = tuple(meta.flatten())

    # pila que guarde el etsado inicial, la posicion vacia y el camino recorrido
    estado_inicial = tuple(puzzle.matriz.flatten())
    stack = [(estado_inicial, puzzle.posicionVacia, [])]
    visitados = set()

    while stack:
        estado_tupla, posVacia, caminoRecorrido = stack.pop()
        #verificar si ya se visito ese camino para poder continuar
        if estado_tupla in visitados:
            continue
        #añadir a visitados el camino actual
        visitados.add(estado_tupla)
        if estado_tupla == objetivo:
            print("¡Solución encontrada!")
            for paso, est in enumerate(caminoRecorrido + [estado_tupla]):
                print(f"\nPaso {paso}:")
                print(np.array(est).reshape(3,3))
            return True

        #Verificar que el camino recorrido no se cicle infinitamente
        if len(caminoRecorrido) >= max_profundidad:
            continue

        #Hacer una copia de la matriz para generar movimientos
        puzzle_actual = MatrizOchoRompeCabezas()
        puzzle_actual.matriz = np.array(estado_tupla).reshape(3,3)
        puzzle_actual.posicionVacia = posVacia

        #Generar hijos o copias de cada movimiento realizado
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

        #Apilar hijos
        for nuevo_estado, nueva_pos in movimientos:
            stack.append((nuevo_estado, nueva_pos, caminoRecorrido + [estado_tupla]))

    print("No se encontró solución dentro del límite de profundidad")
    return False
