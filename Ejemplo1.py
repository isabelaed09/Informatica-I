camisetas = { 1: ["polo", "blanca", 15],
             2: ["polo", "azul", 15],
             3: ["polo", "roja", 15],
             4: ["polo", "amarilla", 15],
             5: ["cuello redondo", "gris", 12],
             6: ["cuello redondo", "negro", 12],
             7: ["cuello redondo", "verde", 12]}

jeans = { 1: ["Azul", 20],
         2: ["verde", 20],
         3: ["cafe", 20],
         4: ["negro", 20],
         5: ["gris", 20]}

zapatos = { 1: ["botas", "cafe", 25],
           2: ["tenis", "azul", 20],
           3: ["botas", "negro", 25],
           4: ["tenis", "blanco", 20]}

compras= []

def datos_comprador():
  while True:
    nombre_apellido = input("Ingrese su nombre y apellido: ")
    identificacion = input("Ingrese su número de identificación (SOLO NÚMEROS): ")
    telefono = input("Ingrese su número de teléfono (SOLO NÚMEROS): ")
    try:
      identificacion = int(identificacion)
      telefono = int(telefono)
      break
    except ValueError:
      print("Por favor ingrese solo números para el telefono y la identificación")
  direccion=input("Ingrese su dirección: ")
  return nombre_apellido, identificacion, direccion, telefono
    
