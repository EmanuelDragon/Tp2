#EXCEPCIONES
#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("ingrese el divisor: "))
try:
    resultado = dividendo / divisor
    print(f"Este es el resultado: {resultado}")
except ZeroDivisionError as e:
    print(f"No puede dividir entre 0: {e}")
except ValueError as a:
    print(f"No puede dividir con una letra: {a}")