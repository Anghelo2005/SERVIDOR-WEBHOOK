import sqlite3
from pydantic import BaseModel

class Multa(BaseModel):
    id_multa: int
    placa: str
    concepto_multa: str
    estado: int
    monto: float

# Lista de 20 objetos Multa con estado 0
multas_data =  [
    Multa(id_multa=1, placa="ABC123", concepto_multa="Exceso de velocidad", estado=0, monto=100.0),
    Multa(id_multa=2, placa="XYZ789", concepto_multa="Estacionamiento indebido", estado=0, monto=150.0),
    Multa(id_multa=3, placa="DEF456", concepto_multa="Semáforo en rojo", estado=0, monto=120.0),
    Multa(id_multa=4, placa="GHI789", concepto_multa="No respetar señal de stop", estado=0, monto=80.0),
    Multa(id_multa=5, placa="JKL012", concepto_multa="Falta de cinturón de seguridad", estado=0, monto=90.0),
    Multa(id_multa=6, placa="MNO345", concepto_multa="Uso de teléfono mientras conduce", estado=0, monto=110.0),
    Multa(id_multa=7, placa="PQR678", concepto_multa="Estacionamiento en zona prohibida", estado=0, monto=130.0),
    Multa(id_multa=8, placa="STU901", concepto_multa="No usar intermitentes al cambiar de carril", estado=0, monto=70.0),
    Multa(id_multa=9, placa="VWX234", concepto_multa="Exceso de velocidad", estado=0, monto=100.0),
    Multa(id_multa=10, placa="YZA567", concepto_multa="Estacionamiento indebido", estado=0, monto=150.0),
    Multa(id_multa=11, placa="BCD890", concepto_multa="Semáforo en rojo", estado=0, monto=120.0),
    Multa(id_multa=12, placa="EFG123", concepto_multa="No respetar señal de stop", estado=0, monto=80.0),
    Multa(id_multa=13, placa="HIJ456", concepto_multa="Falta de cinturón de seguridad", estado=0, monto=90.0),
    Multa(id_multa=14, placa="KLM789", concepto_multa="Uso de teléfono mientras conduce", estado=0, monto=110.0),
    Multa(id_multa=15, placa="NOP012", concepto_multa="Estacionamiento en zona prohibida", estado=0, monto=130.0),
    Multa(id_multa=16, placa="QRS345", concepto_multa="No usar intermitentes al cambiar de carril", estado=0, monto=70.0),
    Multa(id_multa=17, placa="TUV678", concepto_multa="Exceso de velocidad", estado=0, monto=100.0),
    Multa(id_multa=18, placa="WXY901", concepto_multa="Estacionamiento indebido", estado=0, monto=150.0),
    Multa(id_multa=19, placa="ZAB234", concepto_multa="Semáforo en rojo", estado=0, monto=120.0),
    Multa(id_multa=20, placa="CDE567", concepto_multa="No respetar señal de stop", estado=0, monto=80.0),
]

# Conexión a la base de datos
conn = sqlite3.connect('multas.db')
cursor = conn.cursor()

# Insertar cada objeto en la base de datos
for multa in multas_data:
    cursor.execute('''
        INSERT INTO Multas (id_multa, placa, concepto_multa, estado, monto)
        VALUES (?, ?, ?, ?, ?)
    ''', (multa.id_multa, multa.placa, multa.concepto_multa, multa.estado, multa.monto))

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
