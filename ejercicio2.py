# Solicita la ruta del archivo y muestra su contenido
ruta = input("Ingresa la ruta del archivo a leer: ")

try:
    archi1 = open(ruta, "r", encoding="utf-8")
    contenido = archi1.read()
    print("Contenido del archivo:\n", contenido)
    archi1.close()
except FileNotFoundError:
    print("El archivo no existe.")
