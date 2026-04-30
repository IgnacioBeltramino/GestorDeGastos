from fastapi import FastAPI
from gasto import Gasto
from MedioDePago import MedioDePago
from repositorios_gastos import guardar_gasto_en_bd, eliminar_gasto_de_la_db
from repositorio_medioDePago import guarda_medio_de_pago_en_db , eliminar_medioDePago_de_la_bd
from schemas import GastoSchema, MedioDePagoSchema

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
