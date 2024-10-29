
print("Bienvenido al programa de ordenamiento de números")
print("Por favor, ingrese tres números diferentes\n")

# Entrada de datos con validación
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    # Verificar si los números son diferentes
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("\nADVERTENCIA: Ha ingresado números iguales")
        
    print("\nAnálisis de los números ingresados:")
    print(f"Número 1: {num1}")
    print(f"Número 2: {num2}")
    print(f"Número 3: {num3}")
    
    # Ordenamiento
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            mayor, medio, menor = num1, num2, num3
        else:
            mayor, medio, menor = num1, num3, num2
    else:
        if num2 >= num1 and num2 >= num3:
            if num1 >= num3:
                mayor, medio, menor = num2, num1, num3
            else:
                mayor, medio, menor = num2, num3, num1
        else:
            if num1 >= num2:
                mayor, medio, menor = num3, num1, num2
            else:
                mayor, medio, menor = num3, num2, num1
    
    print("\nResultados:")
    print("Números ordenados de mayor a menor:")
    print(f"{mayor} > {medio} > {menor}")
    
    # Extra/adicional
    print("\nInformacion extra:")
    print(f"Número mayor: {mayor}")
    print(f"Número del medio: {medio}")
    print(f"Número menor: {menor}")
    print(f"Diferencia entre mayor y menor: {mayor - menor}")
    print(f"Promedio de los tres números: {(mayor + medio + menor) / 3:.2f}")

except ValueError:
    print("\nERROR: Por favor, ingrese solo números válidos")
    print("Ejemplo de entradas válidas: 15, -3.14, 0, 42.5, etc.")