import random
class Cliente:
    def __init__(self, nombre, apellido, telefono, identificador, activo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
    
    def __str__(self):
        return f"Datos del cliente: {self.identificador} {self.nombre} {self.apellido} {self.telefono} {self.activo}"
          


def quitar_cliente(nombre, apellido, telefono, id_cliente, activo):
    clientes = [nombre, apellido, telefono, id_cliente, activo]
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

def crear_cliente(clientes):
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    telefono = int(input("Introduzca su numero de telefono: "))
    id_cliente = random.randint(1,100)
    activo = True #Este valor será True porque estamos dando de alta a un cliente
    clientes = Cliente(nombre, apellido, telefono, id_cliente, activo)
    return clientes
    
    
    
   
    
    

class Empleado:
    def __init__(self, nombre, apellido, desocupado, lista_de_tareas):
        self.nombre = nombre
        self.apellido = apellido
        self.desocupado = desocupado
        self.lista_de_tareas = lista_de_tareas

def asignar_tarea_empleado(nombre, apellido, desocupado, lista_de_tareas):
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    tareas = input("Introduzca una tarea por hacer: ")
    lista_de_tareas = {}
    desocupado = input("si/no: ")
    lista_de_tareas[tareas] = nombre +" "+ apellido +" "+ desocupado
    return lista_de_tareas


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
    desocupado = None
    lista_de_tareas = {}
    empleado = Empleado(nombre, apellido, desocupado, lista_de_tareas)
    print(empleado)
    return listar_empleados(nombre, apellido, desocupado, lista_de_tareas)