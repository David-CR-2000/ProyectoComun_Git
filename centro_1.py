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
    

    op = input('Introduce una opcion: ')
    match op:
        case '1':
            crear_cancha()


menu()
