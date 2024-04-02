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

def seleccionar_articulo(diccionario):
  while True:
    print("ARTÍCULOS DISPONIBLES")
    for clave, valor in diccionario.items():
      if len(valor) == 3:
        print(f"{clave}: {valor[0]} - {valor[1]} - ${valor[2]}")
      else: 
        print(f"{clave}: {valor[0]} - {valor[1]}")
    try:
      seleccion = int(input("Seleccione el número del artículo que desea comprar: "))
      if seleccion in diccionario:
        break
      else:
        print("Número de artículo no válido")
    

    except ValueError:
      print("Por favor ingrese solo números")
  return diccionario[seleccion]

def calcular_total(compra):
  precios=[]
  for item in compra:
    if len(item) == 3:
      precios.append(item[2])
    else:
      precios.append(item[1])
  total = sum(precios)
  return total

def mostrar_factura(compra,datos_comprador):
  print("\n Factura: ")
  print("\n Datos del comprador \n")
  print("Nombre:", datos_comprador[0])
  print("Identificación:", datos_comprador[1])
  print("Dirección:", datos_comprador[2])
  print("Teléfono:", datos_comprador[3])
  print("Artículos comprados: ")
  for item in compra:
    if len(item) == 3:
      print(f"{item[0]} - {item[1]} - ${item[2]}")
    else:
      print(f"{item[0]} - {item[1]}")
  print("Total de la compra: ", calcular_total(compra))

def main():

    
  
        
