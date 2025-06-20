#Trabajando con archivos de texto en Python
#1. Abrir el archivo en modo creación
arch1=open("datos.txt","w")
arch1.write("Primera linea \n")
arch1.write("Segunda linea \n")
arch1.write("Tercera linea \n")
arch1.close()
print("Fin del programa")
