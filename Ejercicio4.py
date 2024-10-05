class Caja:
    def __init__(self, dinero=0.0):
        self.dinero = dinero

def __add__(self, otra_caja):
    if isinstance(otra_caja, Caja):
        return Caja(self.dinero + otra_caja.dinero)
        return  Notlmplemented

  def __sub__(self, cantidad):
      if isintance(cantidad,(int, float)) and cantidad >0:
          if nuevo_monto >=0:
              return Caja(nuevo_monto)
          else:
              raise ValueError("No hay suficiente dinero en la caja para retirar esa cantidad.")
              return Notlmplemented

def __eq__(self, otra_caja):
    if isintance(otra_caja, Caja):
        return self.dinero == otra_caja.dinero
        return Notlmplemented

def __str__(self):
    return f"La caja tiene{self.dinero}dinero."

class ListaEnlazada:
    
#-------- Clase Anidada - NODO ------------#
    class _Node:
        __slots__ = '_element', '_next' # optimiza el uso de memoria

        def __init__(self, element, next): 
            self._element = element # inicializar el contenido del Nodo
            self._next = next       # referencia al siguiente Nodo

#----------- Métodos de la Lista Enlazada ----------- #

    def __init__(self):
        """Crear una lista vacia.""" 
        self._head = None #Cabeza de la lista
        self._size = 0 # tamaño de la lista

    def __len__(self):
        """Retornar el número de elementos en la lista."""
        return self._size

    def is_empty(self):
        """Retorna True si la lista esta vacia."""
        return self._size == 0

def insertar(self, element):
    ""insertra un elemnto al inicio de la lista."""
    nuevo_nodo = self.Node(element,self._head)
    self._head = nuevo_nodo
    self._size + = 1

    def remover(self, element):
    """Remueve la primera apoaricion de un elemento en la lista."""
    actual = self._head
    previo = None
    while actual  is not None and actual._element !=element:
    
