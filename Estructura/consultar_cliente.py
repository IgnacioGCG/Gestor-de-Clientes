class ConsultarCliente:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        dni = input("Introduce el DNI del cliente a consultar: ")
        for cliente in self.gestor.clientes:
            if cliente["dni"] == dni:
                print(f"Cliente encontrado: DNI: {cliente['dni']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}")
                return
        print("Cliente no encontrado.")
