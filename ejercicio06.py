"""Programa que lea una cadena por teclado y compruebe cada una de las letras si es mayúscula o no."""

palabra = input("Ingrese una palabra: ")

for i, letra in enumerate(palabra):
    if letra.isupper():
        print(f"La letra '{letra}' en la posición {i+1} es mayúscula.")
    else:
        print(f"La letra '{letra}' en la posición {i+1} no es mayúscula.")