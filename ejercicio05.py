"""
Escribe un programa que pida un nombre de usuario y una contraseña
 y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema",
 sino se da un error.
"""
import getpass

while True:
    usuario = getpass.getpass("Ingrese su nombre de usuario: ")
    contrasena = getpass.getpass("Ingrese su contraseña: ")
    usuario1 = getpass.getpass("Por favor ingrese de nuevo su nombre de usuario: ")
    contrasena1 = getpass.getpass("Por favor ingrese de nuevo su contraseña: ")

    if usuario == usuario1 and contrasena == contrasena1:
        print("¡Has entrado al sistema!")
        break
    else:
        print("Error: Usuario o contraseña incorrectos. Intenta nuevamente.")
