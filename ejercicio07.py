"""
Realiza un programa que calcule la potencia, para ello pide por teclado  la base y el exponente. Pueden ocurrir tres cosas:
 * El exponente sea positivo, sólo tienes que imprimir la potencia.
 * El exponente sea 0, el resultado es el que ingreso el usuario.
 * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
base = float(input("Introduce la base(Numero grande): "))
exponente = int(input("Introduce el exponente(Numero pequeño): "))
if exponente > 0:
    resultado = base ** exponente
if exponente == 0:
    resultado = 1
if exponente < 0:
    resultado = 1 / (base ** abs(exponente))
print("El resultado es:", resultado)
