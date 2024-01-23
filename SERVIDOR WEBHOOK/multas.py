import sqlite3

def crear_tabla():
    # Conexión a la base de datos (o creación si no existe)
    conn = sqlite3.connect('multas.db')

    # Creación del cursor
    cursor = conn.cursor()

    # Creación de la tabla Multas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Multas (
            id_multa INTEGER PRIMARY KEY,
            placa varchar(10),
            concepto_multa varchar(250),
            estado bit,
            monto real
        )
    ''')

    # Confirmar la creación de la tabla
    conn.commit()

    # Cerrar la conexión
    conn.close()

crear_tabla()
