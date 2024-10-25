# (Programa que pide un número y dice si es positivo, negativo o 0)

def SignoPoN(num):
  if num > 0:
    return f"El número {num} por lo tanto es positivo."
  elif num < 0:
    return f"El número {num}  por lo tanto es negativo."
  else:
    return "El número  es cero."

try:
  num = float(input("Ingrese un número: "))
  result = SignoPoN(num)
  print(result)
except ValueError:
  print("Por favor, ingrese un número válido, no un caracterer :)")