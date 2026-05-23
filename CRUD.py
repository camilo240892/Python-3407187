from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

clientes = []

class Cliente(BaseModel):
    codigo: int
    nombre: str
    descripcion: str = None

# Mostrar clientes
@app.get("/clientes")
def mostrar_clientes():
    return clientes

# Crear cliente
@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {"mensaje": "Cliente agregado"}

# Actualizar cliente
@app.put("/clientes/{codigo}")
def actualizar_cliente(codigo: int, datos: Cliente):

    for i, cliente in enumerate(clientes):

        if cliente.codigo == codigo:
            clientes[i] = datos
            return {"mensaje": "Cliente actualizado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# Eliminar cliente
@app.delete("/clientes/{codigo}")
def eliminar_cliente(codigo: int):

    for i, cliente in enumerate(clientes):

        if cliente.codigo == codigo:
            clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True) 