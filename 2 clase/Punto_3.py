#EXCEPCIONES
#Escribe un programa que intente acceder a una clave que no existe en un
#diccionario. Si se produce una excepción KeyError, captura la excepción y muestra.
diccionario = {
    "nombre" : "Emanuel",
    "edad" : 19,
    "telefono" : 3885890902
}
try:
    print(diccionario["apellido"])
except KeyError as e:
    print(f"No existe en el diccionario {e}")