# API de Gestión de Clientes, Facturas y Transacciones

## Descripción

Este proyecto consiste en una API REST desarrollada en Python utilizando FastAPI. La aplicación permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) sobre tres entidades principales:

* Clientes
* Facturas
* Transacciones

El objetivo del proyecto es poner en práctica conceptos fundamentales de desarrollo backend, manejo de rutas, validación de datos mediante Pydantic y creación de servicios web con FastAPI que es lo que estamos viendo en las clases.

---

## Tecnologías Utilizadas

* Python 3
* FastAPI
* Pydantic
* Uvicorn

---

## Funcionalidades

### Gestión de Clientes

Permite administrar la información de los clientes mediante los siguientes endpoints:

| Método | Endpoint           | Descripción                |
| ------ | ------------------ | -------------------------- |
| GET    | /clientes          | Mostrar todos los clientes |
| POST   | /clientes          | Crear un cliente           |
| PUT    | /clientes/{codigo} | Actualizar un cliente      |
| DELETE | /clientes/{codigo} | Eliminar un cliente        |

#### Estructura Cliente

```json
{
  "codigo": 1,
  "nombre": "Juan Pérez",
  "descripcion": "Cliente frecuente"
}
```

---

### Gestión de Facturas

Permite registrar y administrar facturas.

| Método | Endpoint       | Descripción                |
| ------ | -------------- | -------------------------- |
| GET    | /facturas      | Mostrar todas las facturas |
| POST   | /facturas      | Crear una factura          |
| PUT    | /facturas/{id} | Actualizar una factura     |
| DELETE | /facturas/{id} | Eliminar una factura       |

#### Estructura Factura

```json
{
  "id": 1,
  "fecha": "2026-06-22",
  "valor_total": 150000,
  "cliente": "Juan Pérez"
}
```

---

### Gestión de Transacciones

Permite registrar las transacciones asociadas a las facturas.

| Método | Endpoint            | Descripción                     |
| ------ | ------------------- | ------------------------------- |
| GET    | /transacciones      | Mostrar todas las transacciones |
| POST   | /transacciones      | Crear una transacción           |
| PUT    | /transacciones/{id} | Actualizar una transacción      |
| DELETE | /transacciones/{id} | Eliminar una transacción        |

#### Estructura Transacción

```json
{
  "id": 1,
  "vr_unitario": 25000,
  "cantidad": 3,
  "factura_id": 1
}
```

---

## Ejecución del Proyecto

### Instalar dependencias

```bash
pip install fastapi uvicorn
```

### Ejecutar la aplicación

```bash
python app.py
```

o

```bash
uvicorn app:app --reload
```

---

## Documentación Automática

Una vez ejecutada la aplicación, FastAPI genera documentación automática:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Objetivo Académico

Este proyecto fue desarrollado con fines educativos para fortalecer competencias en:

* Desarrollo de APIs REST.
* Programación en Python.
* Manejo de rutas HTTP.
* Validación de datos con Pydantic.
* Uso del framework FastAPI.
* Implementación de operaciones CRUD.

---

## Autor

Camilo Berdugo

Este Proyecto Lo Estoy Desarrollando Paso a Paso.
