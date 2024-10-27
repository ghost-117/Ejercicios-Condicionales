"""
Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
la edad es mayor o igual a dieciocho y el sexo es 'F'. 
En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
"""
nota = float(input("Ingrese la nota (0-10): "))
if nota < 0 or nota > 10:
    print("ERROR: La nota debe estar entre 0 y 10")
else:
    # Validación de edad
    edad = int(input("Ingrese la edad: "))
    if edad < 0 or edad > 120:
        print("ERROR: La edad no es válida")
    else:
        # Validación de sexo
        sexo = input("Ingrese el sexo (F/M): ").upper()
        if sexo != "F" and sexo != "M":
            print("ERROR: El sexo debe ser F o M")
        else:
            # Lógica principal con mensajes más detallados
            if nota >= 5:
                if edad >= 18:
                    if sexo == "F":
                        print("\nRESULTADO: ACEPTADA")
                        print("¡Felicitaciones! Cumple con todos los requisitos:")
                        print(f"- Nota aprobada: {nota}/10")
                        print(f"- Mayor de edad: {edad} años")
                        print("- Sexo: Femenino")
                    else:
                        print("\nRESULTADO: POSIBLE")
                        print("Cumple con los requisitos básicos:")
                        print(f"- Nota aprobada: {nota}/10")
                        print(f"- Mayor de edad: {edad} años")
                        print("- Sexo: Masculino")
                else:
                    print("\nRESULTADO: NO ACEPTADA")
                    print("Motivo: No cumple con la edad mínima requerida")
                    print(f"Edad actual: {edad} años (mínimo 18)")
            else:
                print("\nRESULTADO: NO ACEPTADA")
                print("Motivo: No alcanza la nota mínima requerida")
                print(f"Nota actual: {nota}/10 (mínimo 5)")