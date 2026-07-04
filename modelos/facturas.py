from pydantic import BaseModel
from modelos.clientes import Cliente

# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de ...
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se ...
# getattr() es una función nativa de Python. Sirve para obtener el valor de un atributo o propiedad de un obj...

# Crear el modelo transacciones(id, fecha, vr_total, cliente)


class FacturaBase(BaseModel):
    fecha: str
    vr_total: float
    cliente: Cliente


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None