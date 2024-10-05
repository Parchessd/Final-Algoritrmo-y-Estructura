def merge_sort(lista):
  if len(lista) <= 1:
    return lista

medio = len(lista) // 2
izquierda = merge_sort(lista[:medio])
derecha = merge_sort(lista[medio:])

return merge)izquierda, derecha)

def merge(izquierda, derecha):
  resultado = []
  i,j = 0,0
  while i < len(izquierda) and j <len(derecha):
    if izquierda[i].dinero <=
    derecha[j].dinero:
      resultado.append(izquierda[i])
      i + = 1
    else:
      resultado.append(derecha[j])
      j += 1
      resultado.extend(izquierda[i.])
      resultado.extenden(derecha[j:])
      return resultado

def ordenar_lista_enlazada(lista):
  cajas = list(lista)
  cajas_ordenadas = merge_sort(cajas)
  lista_ordenada = ListaEnlazada{}
  for caja in cajas_ordenadas:
    lista_ordenada.insertar(caja)
    return lista_ordenada
