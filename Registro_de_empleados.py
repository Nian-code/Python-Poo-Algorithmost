class registroDotacion():
    
    def __init__(self):
        self.__registro = {}
    
    def agregar(self, empleado):
        self.__registro[empleado.id] = empleado.fecha_dotacion
        print(f"Usuario {empleado.nombre} ha sido agregado a la base")

    @property
    def listar(self):
        print(self.__registro)

    def eliminar(self, empleado):
        if empleado.id in self.__registro:
            del self.__registro[empleado.id]
            print("Se ha eliminado")
        else:
            raise ValueError("Empleado no encontrado")
        
class empleado():

    def __init__(self, nombre, id, fecha_dotacion):
        self.__nombre = nombre
        self.__id = id
        self.__fecha_dotacion = fecha_dotacion
        

    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def fecha_dotacion(self):
        return self.__fecha_dotacion

    @fecha_dotacion.setter
    def set_fecha_dotacion(self, fecha_dotacion):
        self.__fecha_dotacion = fecha_dotacion
        print(f'Se ha ectualizado la fecha de dotacion de {self.__nombre}') 

class empleado_directo(empleado):
    def __init__(self, nombre, id, fecha_dotacion):
        super().__init__(nombre, id, fecha_dotacion)

class empleado_indirecto(empleado):
    def __init__(self, nombre, id, fecha_dotacion):
        super().__init__(nombre, id, fecha_dotacion)

def añadir_listar(registro, empleado):
    registro.agregar(empleado)
    registro.listar

def main():
    registro  = registroDotacion()

    empleado1 = empleado("Oliver", "1", "12-de-diciembre")
    empleado2 = empleado("bernardo", "2", "14-de-diciembre")
    añadir_listar(registro, empleado1)
    añadir_listar(registro, empleado2)

    empleado2.set_fecha_dotacion = "20-de-diciembre" #Setter
    añadir_listar(registro, empleado2)

    empleado3 = empleado_directo("nicoll", "3", "24-de-diciembre")
    añadir_listar(registro, empleado3)

    empleado4 = empleado_indirecto("esteban", "4", "28-de-diciembre")
    añadir_listar(registro, empleado4)

    empleado4.set_fecha_dotacion = "30-de-diciembre" #Setter
    añadir_listar(registro, empleado4)

if __name__ == "__main__":
    main()