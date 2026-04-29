import sqlite3

def conectar_con_la_base (): # CON ESTO SOLO ME CONECTO A LA BASE 
    return sqlite3.connect("GestorDeGastos.db") 



def crear_tabla_gastos(): # FUNCION QUE CREA LA TABLA GASTOS 
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            monto DOUBLE NOT NULL,
            IDMedioDePago INTEGER NOT NULL,
            fecha DATE NOT NULL,
            usuario_id INTEGER NOT NULL
        )
    ''')

def crear_tabla_MediosDePago(): # FUNCION QUE CREA LA TABLA MEDIOS DE PAGO
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mediosDePago (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            usuario_id INTEGER NOT NULL
        )
    ''')

if __name__ == "__main__":
    crear_tabla_gastos()
    crear_tabla_MediosDePago()
    print("Tablas creadas correctamente.")