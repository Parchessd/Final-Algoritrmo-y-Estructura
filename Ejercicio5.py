class iteradorListaEnlazada:
  def __init__(self,cabeza):
    self.actual = cabeza

def __iter__ (self):
  return self

def __next__(self):
  if self.actual is None:
    raise Stoplteration
    caja = self.actual.siguiente
    retrun caja

ListaEnlazada.__iter__= lambda self:
iteradorListaEnlazada(self.cabeza)
