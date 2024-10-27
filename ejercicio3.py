# (Escribe un programa que lea un número e indique si es par o impar)
def par_impar(numero):

  if numero % 2 == 0:
    return f"El número {numero} es par."
  else:
    return f"El número {numero} es impar."
try:
  num = int(input("Ingrese un número entero: "))
  result = par_impar(num)
  print(result)
except ValueError:
  print("Por favor, ingrese un número entero válido (sin decimales y caracteres).")