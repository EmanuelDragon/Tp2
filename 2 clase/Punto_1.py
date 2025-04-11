#EXCEPCIONES
#Escribe un programa que intente dividir dos números. Si el segundo número es cero
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("ingrese el divisor: "))
try:
    resultado = dividendo / divisor
    print(f"Este es el resultado: {resultado}")
except ZeroDivisionError as z:
    print(f"Ocurrios un error ya que intento dividir entre 0: {z}")