import csv


class Escritor:
    def escribir_tablero(tablero, nombre_tablero):
        with open("./tableros/"+nombre_tablero+".csv", "w") as archivo:
            texto = csv.writer(archivo)
            for linea in tablero:
                texto.writerow(linea)

    def escribir_solucion(soluciones, nombre_tablero):
        with open("./soluciones/"+nombre_tablero+"_solucion.csv", "w") as archivo:
            titulos = ["palabra", "x_inicial",
                       "y_inicial", "y_final", "x_final"]
            texto = csv.DictWriter(archivo, fieldnames=titulos)
            texto.writeheader()
            for clave, valor in soluciones.items():
                texto.writerow({
                    "palabra": clave,
                    "x_inicial": valor["x_inicial"],
                    "y_inicial": valor["y_inicial"],
                    "y_final": valor["y_final"],
                    "x_final": valor["x_final"]
                })
