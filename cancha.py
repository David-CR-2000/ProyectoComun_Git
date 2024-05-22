

class Cancha:
    def __init__(self, num_cancha, deporte, precio, habilitada):
        self.num_cancha = num_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []

def cancha_disponible(canchas, num_cancha):
    for cancha in canchas:
        if cancha.num_cancha == num_cancha:
            return False
    return True

def crear_cancha(canchas):
    num_cancha = input('Introduce el numero de cancha: ')
    deporte = input('Introduce el deporte: ')
    precio = input('Introduce el precio: ')
    habilitada = input('Esta habilitada? si/no: ')
    cancha = Cancha(num_cancha, deporte, precio, habilitada)
    if cancha_disponible(canchas, num_cancha):
        canchas.append(cancha)
    else:
        print("La cancha introducida ya existe")

def listar_canchas(canchas):
    deporte = input('Introduce el deporte de las canchas que desea mostrar: ')
    for cancha in canchas:
        if cancha.deporte == deporte:
            print(f'Numero: {cancha.num_cancha}, deporte: {cancha.deporte}, precio:, habilitada: {cancha.habilitada}, reservas: {cancha.reservas}, empleados: {cancha.empleados}')

def quitar_cancha(canchas):
    num = input('Introcuce el número de la cancha que desea quitar: ')
    for cancha in canchas:
        if cancha.num_cancha == num:
            del cancha

