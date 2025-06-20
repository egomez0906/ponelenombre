archi1 = open("datos.txt", "w", encoding="utf-8")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.write("ǩ")  # Alt+269
archi1.close()
