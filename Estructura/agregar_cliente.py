class AgregarCliente:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        dni = input("Introduce el DNI del nuevo cliente: ")
        if any(cliente["dni"] == dni for cliente in self.gestor.clientes):
            print("Ya existe un cliente con ese DNI.")
            return
        nombre = input("Introduce el nombre del cliente: ")
        apellido = input("Introduce el apellido del cliente: ")
        self.gestor.clientes.append({"nombre": nombre, "apellido": apellido, "dni": dni})
        print("Cliente agregado correctamente.")
