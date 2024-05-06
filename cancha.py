class Cancha:
    def __init__(self, num_cancha, deporte, precio, habilitada, reservas, empleados):
        self.num_cancha = num_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = reservas
        self.empleados = empleados
    
    
    def listar_canchas(self):
        pass
    def quitar_cancha(self):
        pass

canchas =[]
centro = []


def crear_cancha(canchas):
    num_cancha = input('Introduce el numero de cancha: ')
    deporte = input('Introduce el deporte: ')
    precio = input('Introduce el precio: ')
    habilitada = input('Esta habilitada? si/no: ')
    cancha = Cancha(num_cancha, deporte, precio, habilitada)
    canchas.append(cancha)

def agregar_cancha(canchas):
    num = input('Introduce el numero de cancha: ')
    for cancha in canchas:
        if cancha.num_cancha == num:
            centro.append(cancha)
        





