class ModificarCliente:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        dni = input("Introduce el DNI del cliente a modificar: ")
        for cliente in self.gestor.clientes:
            if cliente["dni"] == dni:
                cliente["nombre"] = input("Introduce el nuevo nombre: ")
                cliente["apellido"] = input("Introduce el nuevo apellido: ")
                print("Cliente modificado correctamente.")
                return
        print("Cliente no encontrado.")
