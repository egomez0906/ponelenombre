# Lee y muestra el contenido del archivo ascii.txt
try:
    archi1 = open("ascii.txt", "r", encoding="utf-8")
    lineas = archi1.readlines()
    print("Contenido del archivo 'ascii.txt':")
    for linea in lineas:
        print(linea, end='')
    archi1.close()
except FileNotFoundError:
    print("El archivo 'ascii.txt' no existe.")
