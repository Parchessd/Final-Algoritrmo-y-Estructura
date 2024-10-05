def guaradar_datos(diccionario,nombre_archivo):
  with open(nombre_archivo,"w")as
  archivo:
  for clave, valor in diccionario.items{}:
  archivo.write(f"{clave},{valor}/n")

def caragr_datos(nombre_archivo):
  diccionario = {} 
with open(nombre_archivo,'r')as
archivo:
  for linea in archivo:
    clave, valor = linea.strip().split(',')
    diccionario[clave] = valor
    return diccionario
