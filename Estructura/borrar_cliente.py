class BorrarCliente:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        dni = input("Introduce el DNI del cliente a borrar: ")
        for cliente in self.gestor.clientes:
            if cliente["dni"] == dni:
                self.gestor.clientes.remove(cliente)
                print("Cliente borrado correctamente.")
                return
        print("Cliente no encontrado.")
