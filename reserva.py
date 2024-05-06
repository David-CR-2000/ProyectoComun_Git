class Reserva:
    def __init__(self, num_reserva, fecha, cliente, cancha):
        self.num_reserva = num_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
            
    def listar_reservas_cancha(self):
        pass
    def listar_reservas_cliente(self):
        pass
    def mostrar_saldo_cliente(self):
        pass


reservas = []


def crear_reserva(lista, cliente, saldo, cancha):
    if saldo < -2000:
        print('No puede crear la reserva, no tiene suficiente saldo')
    else:
        num_reserva = input('Introduce el numero de reserva: ')
        fecha = input('Introduce la fecha: ')
        reserva = Reserva(num_reserva, fecha, cliente, cancha)
        lista.append(reserva)
        saldo -= 100    # 100 es un precio aleatorio que he puesto, si en el cliente añadimos un atributo saldo hay que cambiar esta función
    







