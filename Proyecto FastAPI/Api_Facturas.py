from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# =====================
# CLIENTES
# =====================

clientes = []

class Cliente(BaseModel):
    codigo: int
    nombre: str
    descripcion: str = None

@app.get("/clientes")
def mostrar_clientes():
    return clientes

@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {"mensaje": "Cliente agregado"}

@app.put("/clientes/{codigo}")
def actualizar_cliente(codigo: int, datos: Cliente):

    for i, cliente in enumerate(clientes):

        if cliente.codigo == codigo:
            clientes[i] = datos
            return {"mensaje": "Cliente actualizado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete("/clientes/{codigo}")
def eliminar_cliente(codigo: int):

    for i, cliente in enumerate(clientes):

        if cliente.codigo == codigo:
            clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# =====================
# FACTURAS
# =====================

facturas = []

class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: str

@app.get("/facturas")
def mostrar_facturas():
    return facturas

@app.post("/facturas")
def crear_factura(factura: Factura):
    facturas.append(factura)
    return {"mensaje": "Factura agregada"}

@app.put("/facturas/{id}")
def actualizar_factura(id: int, datos: Factura):

    for i, factura in enumerate(facturas):

        if factura.id == id:
            facturas[i] = datos
            return {"mensaje": "Factura actualizada"}

    raise HTTPException(status_code=404, detail="Factura no encontrada")

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for i, factura in enumerate(facturas):

        if factura.id == id:
            facturas.pop(i)
            return {"mensaje": "Factura eliminada"}

    raise HTTPException(status_code=404, detail="Factura no encontrada")


# =====================
# TRANSACCIONES
# =====================

transacciones = []

class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int

@app.get("/transacciones")
def mostrar_transacciones():
    return transacciones

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):
    transacciones.append(transaccion)
    return {"mensaje": "Transacción agregada"}

@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, datos: Transaccion):

    for i, transaccion in enumerate(transacciones):

        if transaccion.id == id:
            transacciones[i] = datos
            return {"mensaje": "Transacción actualizada"}

    raise HTTPException(status_code=404, detail="Transacción no encontrada")

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for i, transaccion in enumerate(transacciones):

        if transaccion.id == id:
            transacciones.pop(i)
            return {"mensaje": "Transacción eliminada"}

    raise HTTPException(status_code=404, detail="Transacción no encontrada")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)