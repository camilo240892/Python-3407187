from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship

from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime
# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de ...
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se ...
# getattr() es una función nativa de Python. Sirve para obtener el valor de un atributo o propiedad de un obj...

# Crear el modelo transacciones(id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())

    # cliente: Cliente  # esta es la relacion con el cliente(objeto)
    # transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        import sqlite3

        try:
            conn = sqlite3.connect("bd_clientes.sqlite3")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT cantidad, vr_unitario FROM transaccion WHERE factura_id = ?",
                (self.id,)
            )

            transacciones = cursor.fetchall()

            total = 0

            for cantidad, vr_unitario in transacciones:
                total += cantidad * vr_unitario

            conn.close()

            return total

        except:
            return 0.0


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")