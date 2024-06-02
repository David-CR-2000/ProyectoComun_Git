from cancha import*
from personas import*
from reserva import*



class Centro:
    def __init__(self, nombre, direccion, lista_canchas, lista_clientes):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = lista_canchas
        self.lista_clientes = lista_clientes
        

centro = Centro('Arcipreste', 'Calle 2', [], [])


def menu():
    while True:
        print("Bienvenido al centro de deportes Arcipreste")
        print("1. Agregar cancha")
        print("2. Registrar cliente")
        print("3. Realizar reserva")
        print("4. Mostrar canchas")
        print("5. Asignar tarea a empleados")
        print("6.")
        print("7. Salir")
        # menu donde el usuario seleccionará lo que quiere hacer
        op = int(input("¿Que desea hacer? \n> "))
        match op:
            case 1: 
                crear_cancha()
                
            case 2:
                clientes = crear_cliente(centro.lista_clientes)
                print(clientes)
                
                
            case 3:
                crear_reserva()

            case 4:
                listar_canchas(centro.lista_canchas)
            
            case 5:
                asignar_tarea_empleado()

            case 6:
                pass

            case 7:
                break



menu()