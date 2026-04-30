from datetime import datetime
from passlib.context import CryptContext  # llamo la libreria para hasear contraseñas 
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto") # le doy contexto para como hasear mis claves 

class Usuario:

    def __init__( self, nombre, apellido, correo ,contrasena, id = None):
        self.fechaRegistro = datetime.now()

        try: # VALIDACIONES DEL NOMBRE 
            if (nombre == None or nombre.strip() == ""):
                raise ValueError ("El nombre no puede estar vacia")
            else:
                self.nombre = nombre
        except ValueError as NombreIncorrecto:
            print (NombreIncorrecto)
            raise

        try: # VALIDACIONES DEL APELLIDO 
            if (apellido == None or apellido.strip() == ""):
                raise ValueError ("El apellido no puede estar vacia")
            else:
                self.apellido = apellido
        except ValueError as ApellidoIncorrecto:
            print (ApellidoIncorrecto)
            raise

        try: # VALIDACIONES DEL correo 
            if (correo == None or correo.strip() == ""):
                raise ValueError ("El correo no puede estar vacia")
            else:
                self.correo = correo
        except ValueError as correoIncorrecto:
            print (correoIncorrecto)
            raise

        try: # VALIDACIONES DE LA CONTRASEÑA  
            if ( contrasena == None or contrasena.strip() == ""):
                raise ValueError ("La contraseña no debe estar vacia")
            elif (len(contrasena) < 8):
                raise ValueError("La contraseña no puede tener menos de 8 caracteres")
            else:
                hash = pwd_context.hash(contrasena)
                self.contrasena = hash
        except ValueError as contrasenaIncorrecta:
            print (contrasenaIncorrecta)
            raise




