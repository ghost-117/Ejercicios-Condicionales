"""
Condicionales if:
Estructura:
  if expresion
     instrucciones
     
     if expresion:
       instrucciones 
    else 
       instrucciones   
"""
print("Programa que verifica si un numero es positivo")
n= int(input("Ingrese un numero: "))
if n > 0:
    print("El numero" , n , "es positivo :D")
else:
    print("El numero", n , "es negativo :(")

print("Programa que verifica si un numero es par o impar")
n2=int(input("Ingrese un numero: "))
if n2 % 2==0:
    print("El numero" , n2, "es par")
else:
    print("El numero", n2, "es impar:(")
    