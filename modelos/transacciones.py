from pydantic import BaseModel


# Crear el modelo Transaccion(id, cantidad, vr_unitario, id_factura)
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int


class TransaccionCrear(TransaccionBase):
    pass


class TransaccionEditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase):
    id: int | None = None
    # aqui va la relacion con el modelo cliente(solo un campo)