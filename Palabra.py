class Palabra:
    def __init__(self, solucion):
        self.texto = solucion[0]
        self.x_inicial = int(solucion[1])
        self.y_inicial = int(solucion[2])
        self.y_final = int(solucion[3])
        self.x_final = int(solucion[4])
        self.encontrada = False
        self.tamaño = len(solucion[0])

    def obtener_palabra(self):
        self.encontrada = True
