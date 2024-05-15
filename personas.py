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
        self.desocupado = []
        self.lista_de_tareas = {}

    def registrar_empleado_cancha(self):
        pass

    def asignar_tarea_empleado(self):
        self.lista_de_tareas = {}
        self.lista_de_tareas["Cambiar las redes"] = empleado.nombre
        return self.lista_de_tareas        

    def listar_empleados(self):
        print("Introduce los datos de los empleados desocupados:")
        self.nombre = input("Introduce el nombre: ")
        self.desocupado.append(self.nombre)
        return self.desocupado

    def quitar_empleados(self):
        pass


cliente = Persona(
    nombre= input("Introduce tu nombre: "),
    apellido= input("Introduce tu apellido: "), 
    telefono= int(input("Introduce tu numero de telefono: ")), 
    identificador= None, 
    activo=None)

empleado = Empleado(
    nombre= input("Introduce tu nombre: "), 
    apellido= input("Introduce tu apellido: "), 
    desocupado= [], 
    lista_de_tareas={})   

