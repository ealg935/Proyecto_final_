import random

def contra(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


try:
    longitud_u = int(input("Ingresa un numero de caracteres para tu contraseña(Maximo 70 caracteres): "))
    if longitud_u <= 0 or longitud_u > 70:
        print("Longitud no válida")
        longitud_u = 12

    contrasena_generada = contra(longitud_u)
    print("\nContraseña generada")
    print(f"Longitud: {longitud_u}")
    print(f"Contraseña: {contrasena_generada}")

except ValueError:
    print("Por favor, ingresa un número válido para la longitud.")
    