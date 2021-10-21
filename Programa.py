import os
import csv

from Obtener_Datos import Obtener_Datos
from Generador_Tableros import Generador_Tableros
from Escritor import Escritor
from Juego import Juego


class Programa:
    def main():
        ## Presentación del programa ##
        with open("logo.txt", "r") as archivo:
            for linea in archivo:
                print(linea.rstrip('\n'))
        while input('Apreta Enter para continuar...\n') != "":
            continue

        ## Nombre del usuario ##
        nombre_usuario = Obtener_Datos().obtener_datos_usuario()

        ## Modos del programa ##
        print("MENU PRINCIPAL:\n")
        while True:
            seleccion_menu = input(
                "1. Crear un nuevo Tablero. \n2. Jugar tablero existente. \n3. Salir del juego. \n\n")

            ## 1. Crear un nuevo Tablero ##
            if seleccion_menu == "1":
                tamaño, palabras, nombre_tablero = Obtener_Datos().obtener_datos_tablero()
                tablero, soluciones = Generador_Tableros().generar(tamaño, palabras)
                Escritor.escribir_tablero(tablero, nombre_tablero)
                Escritor.escribir_solucion(soluciones, nombre_tablero)
                for fila in tablero:
                    print(" | ".join(fila))

                print("\n¡TABLERO CREADO CON EXITO!\n\n")

            ## 2. Jugar tablero existente ##
            elif seleccion_menu == "2":
                print("\nTABLEROS DISPONIBLES: \n")
                tableros_disponibles = os.listdir("./tableros/")
                juego_seleccionado = []
                seleccion_juego = ""
                for i in range(len(tableros_disponibles)):
                    print(str(i+1)+". " +
                          tableros_disponibles[i].capitalize().replace(".csv", "").replace("_", " "))
                print("")

                ## Selección de tablero ##
                while True:
                    seleccion_juego = input("Numero de tablero: ")
                    try:
                        seleccion_juego = int(seleccion_juego)-1
                        if 0 <= seleccion_juego < len(tableros_disponibles):
                            break
                        else:
                            print("\nERROR. Selecciona una opción disponible.")
                    except:
                        print("\nERORR. Dato invalido.")

                ## Inicio del juego ##
                with open("./tableros/"+tableros_disponibles[seleccion_juego]) as fichero:
                    lector = csv.reader(fichero)
                    juego_seleccionado.append(
                        [ele for ele in lector if ele != []])
                with open("./soluciones/"+tableros_disponibles[seleccion_juego].replace(".csv", "")+"_solucion.csv") as fichero:
                    lector = csv.reader(fichero)
                    juego_seleccionado.append(
                        [ele for ele in lector if ele != []])
                juego = Juego(juego_seleccionado, nombre_usuario)
                if os.name == "nt":
                    os.system("cls")
                juego.encontrar_palabra()

            ## 3. Salir del juego. ##
            elif seleccion_menu == "3":
                print("\n¡Hasta Pronto, "+nombre_usuario+"!\n")

                break

            ## Errores de selección. ##
            else:
                print("\nERROR. Selecciona una opción disponible.")


if __name__ == "__main__":
    Programa.main()
