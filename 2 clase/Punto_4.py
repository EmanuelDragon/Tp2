#EXCEPCIONES
#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#embargo, también intenta crear el archivo si no existe
try:
    with open("archivo_1.txt", "r") as archivo:
        print("Entre al archivo")
except FileNotFoundError as e:
    print(f"El archvio no existe {e}")
    with open("archivo_2", "w") as archivo2:
        archivo2.write("Archivo creado")
finally:
    print("Archivo creado")