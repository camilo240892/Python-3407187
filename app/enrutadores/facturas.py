from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()

# lista_clientes: list[Cliente] = []#vacia
# lista_facturas: list[Factura] = []


@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas(sesion: Sesion_dependencia):
    #select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, sesion: Sesion_dependencia):

    factura = sesion.get(Factura, factura_id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe.",
        )

    return factura

@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion:Sesion_dependencia):
    # buscar el cliente en bd

    cliente_encontrado = sesion.get(Cliente, cliente_id)
    # mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe.",
        )
        
    # validar datos de la factura-json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)

    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val




# endpoint para editar una factura
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:

            factura_val = Factura.model_validate(
                datos_factura.model_dump()
            )

            factura_val.id = factura_id

            # conservar el cliente asociado
            factura_val.cliente = obj_factura.cliente

            lista_facturas[i] = factura_val

            return factura_val

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id}, no existe."
    )


# endpoint para eliminar una factura
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:

            factura_eliminada = lista_facturas.pop(i)

            return factura_eliminada

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id}, no existe."
    )