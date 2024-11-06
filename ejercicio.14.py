"""
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.
"""
print("Este programa muestra la cantidad de días que tiene el mes correspondiente al número ingresado.\n")

try:
    mes = int(input("Introduce el número del mes (1-12): "))
    if mes < 1:
        
        print("El número ingresado es menor que 1.")
        print("Por favor, ingresa un número entre 1 y 12.")
    else:
        if mes > 12:
            print("El número ingresado es mayor que 12.")
            print("Por favor, ingresa un número entre 1 y 12.")
        else:
            print(f"\n Número de mes válido: {mes}")
            print("\nRESULTADO:")
            if mes == 1:
                print("El mes tiene 31 días")
            else:
                if mes == 2:
                    print("El mes tiene 28 días")
                else:
                    if mes == 3:
                        print("El mes tiene 31 días")
                    else:
                        if mes == 4:
                            print("El mes tiene 30 días")
                        else:
                            if mes == 5:
                                print("El mes tiene 31 días")
                            else:
                                if mes == 6:
                                    print("El mes tiene 30 días")
                                else:
                                    if mes == 7:
                                        print("El mes tiene 31 días")
                                    else:
                                        if mes == 8:
                                            print("El mes tiene 31 días")
                                        else:
                                            if mes == 9:
                                                print("El mes tiene 30 días")
                                            else:
                                                if mes == 10:
                                                    print("El mes tiene 31 días")
                                                else:
                                                    if mes == 11:
                                                        print("El mes tiene 30 días")
                                                    else:
                                                        if mes == 12:
                                                            print("El mes tiene 31 días")
            print(f"- El número de mes ingresado fue: {mes}")            
except ValueError:
    print("\n❌ ERROR: Entrada inválida")
    print("Por favor, ingresa solo números enteros, Ejemplo: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 o 12")