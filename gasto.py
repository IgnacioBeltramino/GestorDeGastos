from datetime import date, datetime


class Gasto:
    #constructor
    def __init__(self, monto, IDmedioDePago, descripcion, fecha, id = None, usuarioID = None):
        fechaActual = date.today() # FIJO LA FECHA Y HORA ACTUAL AL MOMENTO DE LLAMAR AL CONSTRUC
        self.usuarioID = usuarioID
        self.IDmedioDePago = IDmedioDePago

        try: # VALIDACIONES MONTO
            if (monto == None or monto <= 0):
                raise ValueError ("El monto del gasto no puede ser negativo ni 0")
            else:
                self.monto = monto
        except ValueError as montoIncorrecto:
            print (montoIncorrecto)
            raise

        try: # VALIDACIONES DE LA DESCRIPCION
            if (descripcion == None or descripcion.strip() == ""):
                raise ValueError ("La descripcion no puede estar vacia")
            else:
                self.descripcion = descripcion
        except ValueError as DescGastoIncorrecta:
            print (DescGastoIncorrecta)
            raise

        try: # VALIDACIONES DE LA FECHA
            if (fecha > fechaActual):
                raise ValueError ("La fecha del gasto no puede ser mayor a la fecha actual")
            else:
                self.fecha = fecha
        except ValueError as FechaIncorrecta:
            print (FechaIncorrecta)
            raise


