class Caja:
  def__init__(self, dinero=0.0):
  self.dinero = dinero

derf agregar_dinero(self,cantidad):
if cantidad > 0:
  self.dinero += cantidad 
print(f"se han agregado {cantidad} a la caja.")
else:
print("La cantidad de agregar debe ser positiva")

def retirar_dinero(self , cantidad):
  if 0 < cantidad <= self.dinero:
    self.dinero = cantidad
print(f"Se han retirado {cantidad} de la caja.")

def mostar_dinero(self):
  print(f"Dinero de la caja:
  {self.dinero}")

def __add__(self, otra_caja):
  if  isinstance(otra_caja, Caja):
    return Caja(self.dinero + otra_caja.dinero)
    return Notlmplemented

def __sub__(self, cantidad):
if isinstance(cantidad, (int,float)) and cantidad > 0:
  nuevo_monto = self.dinero - cantidad
  if nuevo_monto > = 0:
    return caja(nuevo_monto)
  else:
    raise ValueError("No hay sufuciente dinero en la caja para retirar esa cantidad.")
    return Notlmplemented

def __eq__(self, otra_caja):
  if isintance(otra_caja, Caja):
    return self.dinero ==otra_caja.dinero
    return Notlmplemented

def __str__(self):
  return f"Dinero en la caja:
  {self.dinero}"
caja1 = Caja(100)
caja2 = Caja(50)

print(caja1)
print(caja2)
caja3 = caja1 + caja2
print(caja3)

caja4 = caja1 - 30
print(caja4)

print(caja1 ==  caja2)
print(caja1 == Caja(100))
  
    
