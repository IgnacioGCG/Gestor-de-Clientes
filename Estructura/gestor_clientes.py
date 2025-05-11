from listar_clientes import ListarClientes
from consultar_cliente import ConsultarCliente
from agregar_cliente import AgregarCliente
from modificar_cliente import ModificarCliente
from borrar_cliente import BorrarCliente
from menu import Menu

class GestorClientes:
    def __init__(self):
        self.clientes = [
            {"nombre": "Juan", "apellido": "Pérez", "dni": "12345678A"},
            {"nombre": "Ana", "apellido": "García", "dni": "87654321B"},
            {"nombre": "Luis", "apellido": "Martínez", "dni": "11223344C"}
        ]

        self.listar = ListarClientes(self)
        self.consultar = ConsultarCliente(self)
        self.agregar = AgregarCliente(self)
        self.modificar = ModificarCliente(self)
        self.borrar = BorrarCliente(self)
        self.menu = Menu(self)
