"""
Realiza un programa que pida el dia de la semana (del 1 al 7) y escriba 
el dia correspondiente. 
# Si introducimos otro número nos da un error.
"""
dia = int(input("Introduce el número del día de la semana (en un rango de 1-7): "))

if dia == 1:
    print(" El dia 1 es Lunes")
elif dia == 2:
    print(" El dia 2 es Martes")
elif dia == 3:
    print("El dia 3 es Miércoles")
elif dia == 4:
    print("El dia 4 es Jueves")
elif dia == 5:
    print("El dia 5 es Viernes")
elif dia == 6:
     print("El dia es Sábado")
elif dia == 7:
   print("El dia es Domingo")
else:
    print("Número de día incorrecto,ingrsa un numero valído")                        
if dia <= 5:
    print("- Es un día laborable de la semana")
else:
    print("- Es fin de semana")