from fastapi import FastAPI
from gasto import Gasto
from repositorios_gastos import guardar_gasto_en_bd
from schemas import GastoSchema

app = FastAPI()

@app.post("/nuevoGasto")
def creacion_de_gasto(data: GastoSchema):
    nuevoGasto = Gasto (monto= data.monto, IDmedioDePago= data.IDMedioDePago, descripcion=data.descripcion, fecha= data.fecha)
    guardar_gasto_en_bd(nuevoGasto)