from pydantic import BaseModel
from datetime import date, datetime

class GastoSchema (BaseModel):
    monto : float
    IDMedioDePago : int
    descripcion : str
    fecha : date
    usuarioID : int

class MedioDePagoSchema (BaseModel):
    nombre : str
    descripcion : str
    usuarioID : int

class UsuarioSchema (BaseModel):
    nombre : str
    apellido : str
    correo : str 
    contrasena : str

class LoginSchema (BaseModel):
    correo : str 
    contrasena : str 