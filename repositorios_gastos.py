from gasto import Gasto
from database import conectar_con_la_base


def guardar_gasto_en_bd (gasto):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO gastos (monto, IDMedioDePago, descripcion, fecha, usuario_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (gasto.monto, gasto.IDmedioDePago, gasto.descripcion , gasto.fecha , gasto.usuarioID))
    conn.commit()
    conn.close()

def eliminar_gasto_de_la_db (id: int):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM gastos WHERE id =(?)
    ''', (id,))
    conn.commit()
    conn.close()
