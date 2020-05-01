archivo = open(input("Ingresa el nombre del archivo con extencion:"), "a")
palabra = input("Escriba una palabra: ")
archivo.write(palabra + "\n")
archivo.close()
