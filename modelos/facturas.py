from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime
# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de ...
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se ...
# getattr() es una función nativa de Python. Sirve para obtener el valor de un atributo o propiedad de un obj...

# Crear el modelo transacciones(id, fecha, vr_total, cliente)
class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente  # esta es la relacion con el cliente(objeto)
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        # calcular(cantidad * vr_unitario)
        return 222 

class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None