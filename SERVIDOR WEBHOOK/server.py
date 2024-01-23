from fastapi import FastAPI, HTTPException
from databases import Database

app = FastAPI()

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./multas.db"
database = Database(DATABASE_URL)

# Modelos Pydantic para la validación de datos
from pydantic import BaseModel

class Multa(BaseModel):
    id_multas: int
    placa: str
    concepto_multa: str
    estado: int
    monto: float

# Endpoint para actualizar el estado de la multa
@app.put("/actualizar_estado/{multa_id}")
async def actualizar_estado(multa_id: int):
    # Conectar a la base de datos
    await database.connect()

    # Consultar la multa por ID
    query = "SELECT * FROM Multas WHERE id_multa = :multa_id"
    multa = await database.fetch_one(query=query, values={"multa_id": multa_id})

    if not multa:
        raise HTTPException(status_code=404, detail="Multa no encontrada")

    # Actualizar el estado de la multa a 1
    update_query = "UPDATE Multas SET estado = 1 WHERE id_multa = :multa_id"
    await database.execute(query=update_query, values={"multa_id": multa_id})

    # Desconectar de la base de datos
    await database.disconnect()

    return {"mensaje": f"Estado de la multa {multa_id} actualizado"}

# Endpoint para mostrar la tabla completa
@app.get("/tabla_multas")
async def tabla_multas():
    # Conectar a la base de datos
    await database.connect()

    # Consultar todas las multas
    query = "SELECT * FROM Multas"
    multas = await database.fetch_all(query=query)

    # Desconectar de la base de datos
    await database.disconnect()

    return multas
