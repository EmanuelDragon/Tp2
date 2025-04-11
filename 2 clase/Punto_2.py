#EXCEPCIONES
#PUNTO 2
#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
numero = 20
cadena = "Hola"
try:
    resultado = numero + cadena
except TypeError as e:
    print(f"No puede sumar un numero con una cadena {e}")
else:
    print(resultado)