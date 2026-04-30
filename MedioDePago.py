class MedioDePago:

    def __init__(self, nombre, descripcion, usuarioID, id = None):
        self.usuarioID = usuarioID
        self.id = id

        try: # VALIDACIONES DEL NOMBRE
            if (nombre == None or nombre.strip() == ""):
                raise ValueError ("El nombre del medio de pago no puede estar vacio")
            else:
                self.nombre = nombre
        except ValueError as NombreMedioDePagoIncorrecto:
            print (NombreMedioDePagoIncorrecto)
            raise

        try: # VALIDACIONES DE LA DESCRIPCION
            if (descripcion == None or descripcion.strip() == ""):
                raise ValueError ("La descripcion no puede estar vacia")
            else:
                self.descripcion = descripcion
        except ValueError as DescMedioDePagoIncorrecta:
            print (DescMedioDePagoIncorrecta)
            raise
