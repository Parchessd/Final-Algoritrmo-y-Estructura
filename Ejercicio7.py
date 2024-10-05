def cifrar_texto(texto):
  resultado = []
  for caracter in texto:
    if "a" <=caracter<= "z":
      nuevo_caracter =
      chr((ord(caracter) - ord("A") + 13) % 26 + ord("A"))
      resultado .append(caracter)
      return".join(resultado)

def cifrar_archivo(archivo_origen,archivo_destino="texto_cifrado.txt"):
  try:
witch open(archivo_origen, 'r')as
origen, open(archivo_destin, 'w')as
destino:
for linea in origen:
  linea_cifrada =
  cifrar_texto(linea.strip())
  destino.write(linea_cifrada)
  
