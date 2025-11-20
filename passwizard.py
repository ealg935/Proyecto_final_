def contra(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    contrasena = ""
    indice_base = len(caracteres) // 2
    for i in range(longitud):
        indice_cal = (indice_base + i * longitud) % len(caracteres)
        
        contrasena = contrasena + caracteres[indice_cal]
        
    return contrasena
try:
    longitud_u = int(input("Ingresa un numero de caracteres: "))
    if longitud_u <= 0 or longitud_u > 70:
        print("Longitud no válida")
        longitud_u = 12
    contrasena_generada = contra(longitud_u)
    print("\nContraseña generada")
    print(f"Longitud: {longitud_u}")
    print(f"Contraseña: {contrasena_generada}")

except ValueError:
    print("Por favor, ingresa un número válido para la longitud.")