import sqlite3

def conectar_con_la_base (): # CON ESTO SOLO ME CONECTO A LA BASE
    return sqlite3.connect("GestorDeGastos.db", check_same_thread=False, timeout=10)



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
    conn.commit()
    conn.close()

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
    conn.commit()
    conn.close()

def crear_tabla_usuarios(): # FUNCION QUE CREA LA TABLA usuario 
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            correo TEXT NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tabla_gastos()
    crear_tabla_MediosDePago()
    crear_tabla_usuarios()
    print("Tablas creadas correctamente.")
