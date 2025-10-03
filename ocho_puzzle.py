import numpy as np
import random

class MatrizOchoRompeCabezas():
    def __init__(self):
        numeros = random.sample(range(0,9), 9) #0 es vacio
        # Convertimos en matriz 3x3
        self.matriz = np.array(numeros).reshape(3, 3)
        self.posicionVacia=self.encontrar_posicion_vacia()

    def encontrar_posicion_vacia(self):
        for i in range (0,3):
            for j in range (0,3):
                if self.matriz[i,j] == 0:
                    return i,j

    def se_puede_mover_arriba(self):
        if self.posicionVacia[0] > 0:
            return True
        else:
            return False

    def se_puede_mover_abajo(self):
        if self.posicionVacia[0] < 2:
            return True
        else:
            return False

    def se_puede_mover_derecha(self):
        if self.posicionVacia[1] < 2:
            return True
        else:
            return False

    def se_puede_mover_izquierda(self):
        if self.posicionVacia[1] > 0:
            return True
        else:
            return False

    def mover_arriba(self):
        if self.se_puede_mover_arriba():
            i, j = self.posicionVacia
            self.matriz[i, j] = self.matriz[i - 1, j]
            self.matriz[i - 1, j] = 0
            self.posicionVacia = (i - 1, j)

    def mover_abajo(self):
        if self.se_puede_mover_abajo():
            i, j = self.posicionVacia
            self.matriz[i, j] = self.matriz[i + 1, j]
            self.matriz[i + 1, j] = 0
            self.posicionVacia = (i + 1, j)

    def mover_izquierda(self):
        if self.se_puede_mover_izquierda():
            i, j = self.posicionVacia
            self.matriz[i, j] = self.matriz[i, j - 1]
            self.matriz[i, j - 1] = 0
            self.posicionVacia = (i, j - 1)

    def mover_derecha(self):
        if self.se_puede_mover_derecha():
            i, j = self.posicionVacia
            self.matriz[i, j] = self.matriz[i, j + 1]
            self.matriz[i, j + 1] = 0
            self.posicionVacia = (i, j + 1)
