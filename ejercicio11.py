"""
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
"""
durallamada = float(input("Ingrese la duración de la llamada en minutos: "))
# Calcular el cobro base de la llamada, Cbase =costo base
if durallamada <= 5:
    Cbase = 1
elif durallamada <= 8:
    Cbase = 1 + 0.8 * (durallamada - 5)
elif durallamada <= 10:
    Cbase = 1 + 0.8 * 3 + 0.7 * (durallamada - 8)
else:
    Cbase = 1 + 0.8 * 3 + 0.7 * 2 + 0.5 * (durallamada - 10)
# Obtener el día y turno de la llamada
dia = input("Ingrese el día de la semana (Domingo/Otro): ")
turno = input("Ingrese el turno (Mañana/Tarde): ")

# Calcular el impuesto aplicable
if dia.lower() == "domingo":
    impuesto = 0.03
elif turno.lower() == "mañana":
    impuesto = 0.15
else:
    impuesto = 0.10

# Calcular el total a pagar
total_a_pagar = Cbase * (1 + impuesto)

# Mostrar los resultados
print("Cobro base de la llamada:", Cbase, "euros")
print("Impuesto aplicado:", impuesto * 100, "%")
print("Total a pagar:", total_a_pagar, "euros")