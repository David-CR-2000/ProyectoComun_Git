from cancha import*
from personas import*
from reserva import*


class Centro:
    def __init__(self, nombre, direccion, lista_canchas, lista_clientes):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = lista_canchas
        self.lista_clientes = lista_clientes



cen = Centro('Arcipreste', 'calle_1', [], [])

def menu():
    while True:

        op = input('1. Agregar cancha\n2. Registrar cliente\n3. Realizar reserva\n4. Mostrar canchas segun el deporte\n7. Salir\nIntroduce una opcion: ')
        match op:
            case '1':
                crear_cancha(cen.lista_canchas)
            case '2':
                crear_cliente()
            case '3':
                crear_reserva(reservas, cen.lista_clientes, cen.lista_canchas)
            case '4':
                listar_canchas(cen.lista_canchas)
            case '5':
                pass
            case '6':
                pass
            case '7':
                break


menu()
