"""Programa que lea una cadena por teclado y compruebe si es una letra mayúscula."""

palabra = input("Ingrese una palabra: ")

for i, letra in enumerate(palabra):
    if letra.isupper():
        print(f"La letra '{letra}' en la posición {i+1} es mayúscula.")
    else:
        print(f"La letra '{letra}' en la posición {i+1} no es mayúscula.")