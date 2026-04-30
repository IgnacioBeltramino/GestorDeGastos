from fastapi import FastAPI
from gasto import Gasto
from MedioDePago import MedioDePago
from usuario import Usuario
from repositorios_gastos import guardar_gasto_en_bd, eliminar_gasto_de_la_db
from repositorio_medioDePago import guarda_medio_de_pago_en_db , eliminar_medioDePago_de_la_bd
from repositorio_usuarios import modificar_correo_del_usuario, eliminar_usuario_de_la_db , guardar_usuario_en_la_bd, obtener_contrasena_por_correo
from schemas import GastoSchema, MedioDePagoSchema, UsuarioSchema, LoginSchema
from auth import validar_contrasena , generar_token

app = FastAPI()

@app.post("/nuevoGasto", status_code=201)
def creacion_de_gasto(data: GastoSchema):
    nuevoGasto = Gasto (monto= data.monto, IDmedioDePago= data.IDMedioDePago, descripcion=data.descripcion, fecha= data.fecha, usuarioID = data.usuarioID)
    guardar_gasto_en_bd(nuevoGasto)
    return {"message": "Gasto creado exitosamente"}

@app.delete("/eliminarGasto/{gasto_id}", status_code=201)
def eliminar_gasto(gasto_id: int):
    eliminar_gasto_de_la_db(gasto_id)
    return {"message": "Gasto eliminado exitosamente"}

@app.post("/nuevoMedioDePago", status_code=201)
def creacion_de_MedioDePago(data: MedioDePagoSchema):
    nuevoMedioDePago = MedioDePago (nombre= data.nombre, descripcion= data.descripcion, usuarioID =data.usuarioID)
    guarda_medio_de_pago_en_db(nuevoMedioDePago)
    return {"message": "Medio de pago creado exitosamente"}

@app.delete("/eliminarMedioDePago/{medioDePagoID}", status_code=201)
def eliminar_medioDePago(medioDePagoID: int):
    eliminar_medioDePago_de_la_bd(medioDePagoID)
    return {"message": "Medio de pago eliminado exitosamente"}

@app.post("/nuevoUsuario", status_code=201)
def creacion_de_usuario(data: UsuarioSchema):
    nuevoUser = Usuario (nombre = data.nombre, apellido = data.apellido, correo = data.correo,contrasena = data.contrasena)
    guardar_usuario_en_la_bd(nuevoUser)
    return {"message": "Usuario creado exitosamente"}

@app.delete("/eliminarUsuario/{usuarioID}", status_code=201)
def eliminar_usuario(usuarioID: int):
    eliminar_usuario_de_la_db(usuarioID)
    return {"message": "Usuario eliminado exitosamente"}

@app.post("/modificarCorreoUsuario/{usuarioID}" ,status_code= 201)
def modificar_correo_usuario(nuevoCorreo : str, usuarioID : int):
    modificar_correo_del_usuario(nuevoCorreo, usuarioID)
    return {"message" : "Correo modificado correctamente"}

@app.post("/login" , status_code= 201)
def login (data: LoginSchema):
    if (validar_contrasena(data.correo, data.contrasena) == True):
        token = generar_token(data.correo)
        return {"Token" : token}
    else:
        return ("Acceso denegado")