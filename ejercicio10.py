"""
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
sin importar el número de alumnos. 
Realice un programa que permita determinar el pago a la compañía de autobuses 
y lo que debe pagar cada alumno por el viaje.
"""
Nalum = int(input("Ingrese el número de alumnos que van a viajar: "))
# Cálculo el pago
if Nalum >= 100:
    Pagocomp =Nalum * 65
    Pagoalumn = 65
elif Nalum >= 50 and Nalum <= 99:
    Pagocomp = Nalum * 70
    Pagoalumn = 70
elif Nalum >= 30 and Nalum <= 49:
    Pagocomp = Nalum * 95
    Pagoalumn = 95
else:
    Pagocomp = 4000
    Pagoalumn =  Pagocomp / Nalum

# Mostrar resultados
print("El pago total a la compañia es de:",  Pagocomp, "euros")
print("Pago por alumno:", Pagoalumn, "euros")