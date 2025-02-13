from math import nan


def calcular_cuotas(cuota_evento):
    # Calcular la probabilidad impl�cita del evento
    probabilidad_evento = 1 / cuota_evento
    
    # Calcular la probabilidad del evento contrario
    probabilidad_no_evento = 1 - probabilidad_evento
    
    # Calcular la cuota del evento contrario
    cuota_no_evento = 1 / probabilidad_no_evento
    
    return round(cuota_evento, 2), round(cuota_no_evento, 2)

# Ejemplo de uso
while 1:  
  cuota_original = input("Cuota de que el evento ocurra (quit para salir): ")
  if cuota_original == "quit": 
     break
  try:
     cuota_original = float(cuota_original)
  except:
     print("el valor de entrada no es un número, introduce un número o 'quit' para salir")
     continue
  cuotas = calcular_cuotas(cuota_original)
  print(f"Cuotas justas: {cuotas}")
