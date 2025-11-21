import random

historial = []

def contra(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


while True:
    try:
        print("\n--- PassWizard ---")
        print("1. Crear nueva contraseña")
        print("2. Ver historial de contraseñas")
        print("3. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            longitud_u = int(input("Ingresa un número de caracteres (máximo 70): "))

            if longitud_u <= 0 or longitud_u > 70:
                print("Longitud no válida. Usando 12 caracteres por defecto.")
                longitud_u = 12

            contrasena_generada = contra(longitud_u)
            historial.append(contrasena_generada)  

            print("\nContraseña generada:")
            print(f"Longitud: {longitud_u}")
            print(f"Contraseña: {contrasena_generada}")

        elif opcion == 2:
            if len(historial) == 0:
                print("\nNo hay contraseñas en el historial todavía.")
            else:
                print("\n--- Historial de Contraseñas ---")
                for i, c in enumerate(historial, start=1):
                    print(f"{i}. {c}")

        elif opcion == 3:
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

    except ValueError:
        print("Por favor, ingresa un número válido.")
