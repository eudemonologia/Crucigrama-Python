from Palabra import Palabra


class Tablero:
    def __init__(self, juego_seleccionado):
        self.tablero, self.soluciones = juego_seleccionado
        self.palabras = {solucion[0]: Palabra(
            solucion) for solucion in juego_seleccionado[1][1:]}

    def imprimir(self):
        for linea in self.tablero:
            print(" | ".join(linea))

    def encontrar_palabra(self, palabra_encontrada):
        palabra = self.palabras[palabra_encontrada]
        palabra.obtener_palabra()
        if palabra.x_inicial != palabra.x_final:
            for i in range(palabra.tamaño):
                self.tablero[palabra.y_inicial][palabra.x_inicial +
                                                i] = self.tablero[palabra.y_inicial][palabra.x_inicial+i].upper()
        if palabra.y_inicial != palabra.y_final:
            for i in range(palabra.tamaño):
                self.tablero[palabra.y_inicial +
                             i][palabra.x_inicial] = self.tablero[palabra.y_inicial+i][palabra.x_inicial].upper()
