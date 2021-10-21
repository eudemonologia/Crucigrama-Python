import random


class Generador_Tableros:

    def generar(self, numero, palabras):
        tablero = []
        soluciones = {}
        letras = set()

        ## Iniciar Tablero vacío ##
        for i in range(numero):
            fila = []
            for k in range(numero):
                fila.append("")
            tablero.append(fila)

        ## Colocar palabras al Tablero ##
        for palabra in palabras:
            random_n = int(random.random() * numero)
            while (random_n > numero - len(palabra)) or (tablero[random_n][random_n] != ""):
                random_n = int(random.random() * numero)
            sorteo = int(random.random() * 2)
            if sorteo == 0:
                for i in range(len(palabra)):
                    tablero[random_n][random_n + i] = palabra[i]
                soluciones[palabra] = {"x_inicial": random_n, "y_inicial": random_n,
                                       "y_final": random_n, "x_final": random_n + len(palabra)}
            elif sorteo == 1:
                for i in range(len(palabra)):
                    tablero[random_n + i][random_n] = palabra[i]
                soluciones[palabra] = {"x_inicial": random_n, "y_inicial": random_n,
                                       "y_final": random_n + len(palabra), "x_final": random_n}

        ## Rellenar espacios del Tablero ##
        for palabra in palabras:
            letras.update([letra for letra in palabra])
        for i in range(numero):
            for k in range(numero):
                index = int(random.random() * len(list(letras)))
                if tablero[i][k] == "":
                    tablero[i][k] = list(letras)[index]

        return tablero, soluciones
