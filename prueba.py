import secrets
import string

# Historial de contraseñas generadas
historial = []

def generar_contraseña(longitud, mayus, minus, nums, especiales):
    caracteres = ""
    seleccionados = []

    if mayus:
        caracteres += string.ascii_uppercase
        seleccionados.append(string.ascii_uppercase)
    if minus:
        caracteres += string.ascii_lowercase
        seleccionados.append(string.ascii_lowercase)
    if nums:
        caracteres += string.digits
        seleccionados.append(string.digits)
    if especiales:
        caracteres += string.punctuation
        seleccionados.append(string.punctuation)

    if not caracteres:
        return "Error: No seleccionaste ningún tipo de carácter."

    if longitud < len(seleccionados):
        return "Error: La longitud es demasiado corta para incluir todos los tipos seleccionados."

    contraseña = []

    # Garantizar al menos un carácter de cada categoría seleccionada
    for grupo in seleccionados:
        contraseña.append(secrets.choice(grupo))

    # Rellenar el resto de la contraseña
    for _ in range(longitud - len(seleccionados)):
        contraseña.append(secrets.choice(caracteres))

    # Mezclar los caracteres para que no queden en orden
    secrets.SystemRandom().shuffle(contraseña)

    contraseña_final = "".join(contraseña)
    historial.append(contraseña_final)
    return contraseña_final


def guardar_en_archivo():
    if not historial:
        print("No hay contraseñas para guardar.")
        return

    # "a" = append → no borra lo anterior
    with open("historial_passwizard.txt", "a") as f:
        for c in historial:
            f.write(c + "\n")

    print("Contraseñas guardadas correctamente en historial_passwizard.txt")


def menu():
    while True:
        print("\n===== PASSWIZARD 🔐 =====")
        print("1. Generar contraseña")
        print("2. Ver historial")
        print("3. Guardar historial en archivo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                longitud = int(input("Longitud de la contraseña: "))

                mayus = input("¿Incluir MAYÚSCULAS? (s/n): ").lower() == "s"
                minus = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
                nums = input("¿Incluir números? (s/n): ").lower() == "s"
                especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == "s"

                if longitud <= 0:
                    print("La longitud debe ser mayor a 0.")
                    continue

                resultado = generar_contraseña(longitud, mayus, minus, nums, especiales)
                print(f"\n🔑 Tu contraseña es: {resultado}")

            except ValueError:
                print("Error: ingresa un número válido para la longitud.")

        elif opcion == "2":
            print("\n📜 Historial de contraseñas:")
            if not historial:
                print("Aún no has generado contraseñas.")
            else:
                for c in historial:
                    print("•", c)

        elif opcion == "3":
            guardar_en_archivo()

        elif opcion == "4":
            print("¡Gracias por usar PassWizard! ✨")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


# Ejecutar el programa
menu()