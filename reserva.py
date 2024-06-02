class Reserva:
    def __init__(self, num_reserva, fecha, cliente, cancha):
        self.num_reserva = num_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
            
    
    
    def mostrar_saldo_cliente(self):
        pass


reservas = []

def reserva_disponible(reservas, fecha, cancha):
    for reserva in reservas:
            if reserva.fecha == fecha and reserva.cancha == cancha:
                return False
    return True
#antiguo codigo de crear reserva
"""
def crear_reserva(reservas, cliente, saldo, cancha):
    if saldo < -2000:
        print('No puede crear la reserva, no tiene suficiente saldo')
    else:
        num_reserva = input('Introduce el numero de reserva: ')
        fecha = input('Introduce la fecha: ')

        if reserva_disponible(reservas, fecha):
            reserva = Reserva(num_reserva, fecha, cliente, cancha)
            reservas.append(reserva)
            saldo -= 100    # 100 es un precio aleatorio que he puesto, si en el cliente añadimos un atributo saldo hay que cambiar esta función
        else:
            print('Ya hay una para ese dia')
"""
def crear_reserva(reservas, clientes, canchas):
    id = input('Introduce el identificador del cliente: ')
    num_cancha = input('Introduce el numero de cancha: ')
    for cliente in clientes:
        if cliente.identificador == id:
            for cancha in canchas:
                if cancha.num_cancha == num_cancha:
                    if cliente.saldo < -2000:
                        print('No puede crear la reserva, no tiene suficiente saldo')
                    else:
                        num_reserva = input('Introduce el numero de reserva: ')
                        fecha = input('Introduce la fecha: ')

                        if reserva_disponible(reservas, fecha, cancha):
                            reserva = Reserva(num_reserva, fecha, cliente, cancha)
                            reservas.append(reserva)
                            cliente.saldo -= 100    # Tendriamos que poner un atributo saldo en el cliente para que esto funcionara bien
                        else:
                            print('Ya hay una para ese dia')


def listar_reservas_cancha(reservas):
    num = input('Introduce el número de cancha: ')
    for reserva in reservas:
        if reserva.cancha.num_cancha == num:
            print(f'Numero: {reserva.num_reserva}\nFecha: {reserva.fecha}\nCliente: {reserva.cliente.nombre}\nCancha: {reserva.cancha.num_cancha}\n')
    

def listar_reservas_cliente(reservas):
    id = input('Introduce el identificador del cliente: ')
    for reserva in reservas:
        if reserva.cliente.identificador == id:
            print(f'Numero: {reserva.num_reserva}\nFecha: {reserva.fecha}\nCliente: {reserva.cliente.nombre}\nCancha: {reserva.cancha.num_cancha}\n')