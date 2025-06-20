# Solicita el nombre del archivo y permite ingresar frases hasta que el usuario escriba 'salir'
ruta = input("Ingresa el nombre del archivo: ")
archi1 = open(ruta, "a", encoding="utf-8")

frase = input("Escribe una frase (o 'salir' para terminar): ")
if frase.lower() != "salir":
    archi1.write(frase + "\n")

    frase = input("Escribe otra frase (o 'salir' para terminar): ")
    if frase.lower() != "salir":
        archi1.write(frase + "\n")

        frase = input("Escribe otra frase (o 'salir' para terminar): ")
        if frase.lower() != "salir":
            archi1.write(frase + "\n")
          

archi1.close()
print("Frases guardadas correctamente.")
