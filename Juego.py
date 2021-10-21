
import os

from Jugador import Jugador
from Tablero import Tablero


class Juego:
    def __init__(self, juego_seleccionado, nombre_usuario):
        self.tablero = Tablero(juego_seleccionado)
        self.usuario = Jugador(nombre_usuario)
        self.palabras_encontradas = []

    def imprimir(self):
        print("\n########## ENCUENTRA TODAS LAS PALABRAS ###########\n\n")
        self.tablero.imprimir()
        self.usuario.imprimir()
        if len(self.palabras_encontradas) > 0:
            print("Palabras encontradas: " +
                  ", ".join(self.palabras_encontradas))

    def encontrar_palabra(self):
        while (self.usuario.intentos > 0) and (self.usuario.puntos != len(self.tablero.palabras)):
            self.imprimir()
            palabra_encontrada = input("Palabra: ").replace(" ", "").lower()
            if palabra_encontrada == "fin":
                break
            try:
                self.tablero.encontrar_palabra(palabra_encontrada)
                print("\n¡PALABRA ENCONTRADA!\n")
                self.palabras_encontradas.append(palabra_encontrada)
                self.usuario.sumar_punto()
            except:
                print("\n¡FALLASTE!\n")
                self.usuario.restar_intento()
        self.terminar_juego()

    def terminar_juego(self):
        palabras_faltantes = [palabra.texto for palabra in self.tablero.palabras.values(
        ) if palabra.encontrada == False]
        if self.usuario.puntos == len(self.tablero.palabras):
            self.tablero.imprimir()
            self.usuario.imprimir_ganador()
            print("Palabras encontradas: " +
                  ", ".join(self.palabras_encontradas))
            print("\n¡GANASTE!\n")

        elif self.usuario.intentos == 0:
            self.tablero.imprimir()
            self.usuario.imprimir_perdedor()
            if len(self.palabras_encontradas) > 0:
                print("Palabras encontradas: " +
                      ", ".join(self.palabras_encontradas))
            print("Palabras no encontradas: " +
                  ", ".join(sorted(palabras_faltantes)))
            print("\n¡PERDISTE!\n")

        else:
            self.tablero.imprimir()
            self.usuario.imprimir_ganador()
            if len(self.palabras_encontradas) > 0:
                print("Palabras encontradas: " +
                      ", ".join(self.palabras_encontradas))
            print("Palabras no encontradas: " +
                  ", ".join(sorted(palabras_faltantes)))
            print("\nJUEGO TERMINADO\n")
