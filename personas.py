class Persona:
    def __init__(self, nombre, apellido, telefono, identificador, activo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
        
def agregar_cliente(nombre, apellido, telefono):
    clientes = []
    clientes.append(nombre)
    clientes.append(apellido)
    clientes.append(telefono)
    return clientes

def quitar_cliente(nombre, apellido, telefono):
    clientes = [nombre, apellido, telefono]
    del clientes
    return clientes

def listar_clientes_morosos():
    print("Clientes morosos")
    morosos = []
    nombre_moroso1, nombre_moroso2, nombre_moroso3 = "Fernando", "Pablo", "Andrés"
    apellido_moroso1, apellido_moroso2, apellido_moroso3 = "Gonzalez", "García", "Gutierrez"
    telefono_moroso1, telefono_moroso2, telefono_moroso3 = 649248822, 697662501, 644002505
    morosos.append(nombre_moroso1)
    morosos.append(apellido_moroso1)
    morosos.append(telefono_moroso1)
    morosos.append(nombre_moroso2)
    morosos.append(apellido_moroso2)
    morosos.append(telefono_moroso2)
    morosos.append(nombre_moroso3)
    morosos.append(apellido_moroso3)
    morosos.append(telefono_moroso3)
    return morosos

def crear_cliente():
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    telefono = int(input("Introduzca su numero de telefono: "))
    clientes = Persona(nombre, apellido, telefono)
    print(clientes)
    return agregar_cliente(nombre, apellido, telefono)

class Empleado:
    def __init__(self, nombre, apellido, desocupado, lista_de_tareas):
        self.nombre = nombre
        self.apellido = apellido
        self.desocupado = desocupado
        self.lista_de_tareas = lista_de_tareas

def asignar_tarea_empleado(nombre, apellido):
    tareas = {}
    tareas["Cambiar redes"] = nombre +" "+ apellido
    return tareas


def listar_empleados(nombre, apellido):
    lista_empleados = []
    lista_empleados.append(nombre)
    lista_empleados.append(apellido)
    return lista_empleados

def quitar_empleados(nombre, apellido):
    lista_empleados = [nombre, apellido]
    del lista_empleados
    return lista_empleados


def registrar_empleado_cancha():
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    empleado = Empleado(nombre, apellido)
    print(empleado)
    return listar_empleados(nombre, apellido)