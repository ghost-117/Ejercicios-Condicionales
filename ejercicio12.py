"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".
"""
print("Simulador de Dado de 6 Caras")
print("Este programa muestra la cara opuesta del número que ingreses")
print("Recuerda: Las caras opuestas son 1-6, 2-5 y 3-4")
print("-" * 50)

try:
    numero = int(input("\nIntroduce el número del dado (1-6): "))
    
    print("\nAnalizando el número...")
    
    if numero < 1:
        print("\n❌ ERROR: número incorrecto.")
        print("El número ingresado es menor que 1")
        print("Por favor, ingresa un número entre 1 y 6")
    else:
        if numero > 6:
            print("\n❌ ERROR: número incorrecto.")
            print("El número ingresado es mayor que 6")
            print("Por favor, ingresa un número entre 1 y 6")
        else:
            print(f"\n✅ Número ingresado válido: {numero}")
            print("Calculando cara opuesta...")
            print("\nEL RESULTADO:")
            
            if numero == 1:
                print("La cara opuesta es: SEIS")
                print("Pareja de caras opuestas: 1-6")
            else:
                if numero == 2:
                    print("La cara opuesta es: CINCO")
                    print("Pareja de caras opuestas: 2-5")
                else:
                    if numero == 3:
                        print("La cara opuesta es: CUATRO")
                        print("Pareja de caras opuestas: 3-4")
                    else:
                        if numero == 4:
                            print("La cara opuesta es: TRES")
                            print("Pareja de caras opuestas: 3-4")
                        else:
                            if numero == 5:
                                print("La cara opuesta es: DOS")
                                print("Pareja de caras opuestas: 2-5")
                            else:
                                if numero == 6:
                                    print("La cara opuesta es: UNO")
                                    print("Pareja de caras opuestas: 1-6")
            
            print("\nInformación adicional:")
            if numero % 2 == 0:
                print("- Has ingresado un número par")
            else:
                print("- Has ingresado un número impar")
except ValueError:
    print("\n❌ ERROR: Entrada inválida")
    print("Por favor, ingresa solo números enteros, ejemplo: 1, 2, 3, 4, 5 o 6")
   