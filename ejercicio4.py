# Escribe la lista de caracteres ASCII (0 a 127) en un archivo
archi1 = open("ascii.txt", "w", encoding="utf-8")
for i in range(128):
    archi1.write(str(i) + ": " + chr(i) + "\n")
archi1.close()
print("Archivo 'ascii.txt' creado con los caracteres ASCII.")
