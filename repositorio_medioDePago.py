from MedioDePago import MedioDePago
from database import conectar_con_la_base

def guarda_medio_de_pago_en_db(medio_de_pago):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mediosDePago (nombre, descripcion, usuario_id)
        VALUES (?, ?, ?)
    ''', (medio_de_pago.nombre, medio_de_pago.descripcion, medio_de_pago.usuarioID))
    conn.commit()
    conn.close()

def eliminar_medioDePago_de_la_bd (id: int):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM mediosDePago WHERE id =(?)
    ''', (id,))
    conn.commit()
    conn.close()