class Jugador:
    def __init__(self, nombre_usuario):
        self.nombre = nombre_usuario
        self.intentos = 3
        self.puntos = 0

    def imprimir(self):
        print("\n\n"+self.nombre.upper() + "\nTienes " +
              str(self.intentos)+" intentos restantes.\nTu puntaje actual es "+str(self.puntos)+".\n")

    def sumar_punto(self):
        self.puntos += 1

    def restar_intento(self):
        self.intentos -= 1

    def imprimir_ganador(self):
        print("\n\n"+self.nombre.upper() + "\nTe quedaron " +
              str(self.intentos)+" intentos.\nTu puntaje final es "+str(self.puntos)+".\n")

    def imprimir_perdedor(self):
        print("\n\n"+self.nombre.upper() +
              "\nTe quedaste sin intentos.\nTu puntaje final fue "+str(self.puntos)+".\n")
