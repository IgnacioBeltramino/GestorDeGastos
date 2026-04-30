from database import conectar_con_la_base
from usuario import Usuario

def guardar_usuario_en_la_bd (usuario):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nombre, apellido, correo, contrasena)
        VALUES (?, ?, ?, ?)
    ''', (usuario.nombre, usuario.apellido, usuario.correo , usuario.contrasena))
    conn.commit()
    conn.close()

def eliminar_usuario_de_la_db (id: int):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE id =(?)
    ''', (id,))
    conn.commit()
    conn.close()

def modificar_correo_del_usuario(correo : str, id: int):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios SET correo = ? WHERE id = ?
    ''', (correo,id))
    conn.commit()
    conn.close()

def obtener_contrasena_por_correo(correo:str):
    conn = conectar_con_la_base()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT contrasena from usuarios where correo = (?)
    ''', (correo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

