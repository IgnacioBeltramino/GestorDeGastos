from usuario import Usuario
from repositorio_usuarios import obtener_contrasena_por_correo
from passlib.context import CryptContext  # llamo la libreria para hasear contraseñas 
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto") # le doy contexto para como hasear mis claves 
from jose import jwt # libreria utilizada para generar el token
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def validar_contrasena(correo, contrasena_a_validar):
    contrasena_del_usuario = obtener_contrasena_por_correo(correo)
    if (contrasena_del_usuario is None):
        return ("Clave incorrecta")
    else:
        contraseña_correcta = pwd_context.verify(contrasena_a_validar, contrasena_del_usuario[0])# esto guarda true o false
        return contraseña_correcta
    

def generar_token (correo: str):
    payload = {"sub": correo}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

