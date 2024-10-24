# programa que pida dos números e indique Cuál es el mayor
#  Si los dos son iguales que muestre el mensaje "Son iguales"

def Comparacionnum(num1, num2):
  """Compara dos números y devuelve un mensaje indicando cuál es mayor o si son iguales."""
  if num1 > num2:
    return "El primer número es mayor."
  elif num1 < num2:
    return "El segundo número es mayor."
  else:
    return "Los dos números son iguales."

try:
  numero1 = float(input("Ingrese el primer número: "))
  numero2 = float(input("Ingrese el segundo número: "))
  resultado = Comparacionnum(numero1, numero2)
  print(resultado)
except ValueError:
  print("Por favor, ingrese solo números.")