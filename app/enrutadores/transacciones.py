from fastapi import APIRouter, HTTPException
from ..modelos.transacciones import (
    Transaccion,
    TransaccionCrear,
    TransaccionEditar
)
from ..modelos.facturas import Factura
from ..listas import lista_facturas, lista_transacciones

rutas_transacciones = APIRouter()


@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones


@rutas_transacciones.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == transaccion_id:
            return obj_transaccion

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {transaccion_id}, no existe."
    )


@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):

    factura_encontrada = None

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrada:
        raise HTTPException(
            status_code=400,
            detail=f"La factura con id {factura_id}, no existe."
        )

    transaccion_val = Transaccion.model_validate(
        datos_transaccion.model_dump()
    )

    transaccion_val.id = len(lista_transacciones) + 1
    transaccion_val.factura_id = factura_id

    lista_transacciones.append(transaccion_val)

    factura_encontrada.transacciones.append(transaccion_val)

    return transaccion_val
@rutas_transacciones.patch("/transacciones/{transaccion_id}", response_model=Transaccion)
async def editar_transaccion(
    transaccion_id: int,
    datos_transaccion: TransaccionEditar
):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == transaccion_id:

            transaccion_val = Transaccion.model_validate(
                datos_transaccion.model_dump()
            )

            transaccion_val.id = transaccion_id
            transaccion_val.factura_id = obj_transaccion.factura_id

            lista_transacciones[i] = transaccion_val

            return transaccion_val

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {transaccion_id}, no existe."
    )


@rutas_transacciones.delete("/transacciones/{transaccion_id}", response_model=Transaccion)
async def eliminar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == transaccion_id:

            transaccion_eliminada = lista_transacciones.pop(i)

            return transaccion_eliminada

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {transaccion_id}, no existe."
    )

