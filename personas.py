class Persona:
    def __init__(self, nombre, apellido, telefono, identificador, activo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
        
    
    def crear_cliente(self):
        pass

    def agregar_cliente(self):
        pass

    def quitar_cliente(self):
        pass

    def listar_clientes_morosos(self):
        pass

class Empleado:
    def __init__(self, nombre, apellido, desocupado, lista_de_tareas):
        self.nombre = nombre
        self.apellido = apellido
        self.desocupado = desocupado
        self.lista_de_tareas = lista_de_tareas

    def registrar_empleado_cancha(self):
        pass

    def asignar_tarea_empleado(self):
        pass

    def listar_empleados(self):
        pass

    def quitar_empleados(self):
        pass