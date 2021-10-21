class Obtener_Datos:
    def obtener_datos_tablero(self):

        ## Pedir el tamaño del crucigrama ##
        tamaño = ""
        while True:
            tamaño = input("Número de filas y columnas: ")
            try:
                tamaño = int(tamaño)
                if tamaño < 15:
                    print("\nERROR. El tamaño debe ser mayor a 15x15.")
                else:
                    break
            except:
                print("\nERROR. No es un número válido.")
        print("\nTu tablero será de: "+str(tamaño)+"x"+str(tamaño)+"\n")

        ## Pedir las palabras del crucigrama ##
        palabras = []
        for i in range(int(tamaño/3)):
            while True:
                palabra = input("Ingresa una palabra: ").lower()
                if palabra == "":
                    print("\nERROR. La palabra no puede estar vacía.")
                elif len(palabra) > int(tamaño/3):
                    print("\nERROR. La palabra debe contar con menos de " +
                          str(int(tamaño/3))+" caracteres.")
                else:
                    break
            if palabra == "fin":
                break
            else:
                palabras.append(palabra)
        print("\nTus palabras a buscar son: " + ", ".join(palabras)+".\n")

        ## Pedir las nombre del crucigrama ##
        nombre_tablero = ""
        while True:
            nombre_tablero = input("Nombre del tablero: ")
            if nombre_tablero == "":
                print("\nERROR. El nombre del tablero no puede estar vacía")
            elif len(nombre_tablero) > 30:
                print(
                    "\nERROR. El nombre del tablero no puese superar los 30 caracteres.")
            else:
                break
        print("\nEl nombre de tu tablero será: "+nombre_tablero+". \n")

        return tamaño, palabras, nombre_tablero

    def obtener_datos_usuario(self):

        ## Pedir nombre del usuario ##
        nombre_usuario = ""
        while True:
            nombre_usuario = input("Nombre del jugador: ").capitalize()
            if nombre_usuario == "":
                print("\nERROR. El nombre del jugador no puede estar vacía")
            elif len(nombre_usuario) > 40:
                print(
                    "\nERROR. El nombre del jugador no puese superar los 40 caracteres.")
            else:
                break
        print("\n¡Bienvenido, "+nombre_usuario+"! \n")
        return nombre_usuario
