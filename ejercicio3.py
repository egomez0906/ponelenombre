# Añade texto a un archivo hasta que el usuario escriba 'salir'
ruta = input("Ingresa el nombre del archivo: ")
archi1 = open(ruta, "a", encoding="utf-8")

linea = input("Escribe una línea (o 'salir' para terminar): ")
if linea.lower() != "salir":
    archi1.write(linea + "\n")

    linea = input("Escribe otra línea (o 'salir' para terminar): ")
    if linea.lower() != "salir":
        archi1.write(linea + "\n")

        linea = input("Escribe otra línea (o 'salir' para terminar): ")
        if linea.lower() != "salir":
            archi1.write(linea + "\n")

archi1.close()
print("Texto añadido correctamente.")
