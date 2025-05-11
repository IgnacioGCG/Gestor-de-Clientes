class ListarClientes:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        print("\nLista de clientes:")
        for cliente in self.gestor.clientes:
            print(f"DNI: {cliente['dni']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}")
        print()
