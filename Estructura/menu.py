class Menu:
    def __init__(self, gestor):
        self.gestor = gestor

    def ejecutar(self):
        while True:
            print("\nGestor de Clientes")
            print("1. Listar clientes")
            print("2. Consultar cliente")
            print("3. Agregar cliente")
            print("4. Modificar cliente")
            print("5. Borrar cliente")
            print("6. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.gestor.listar.ejecutar()
            elif opcion == "2":
                self.gestor.consultar.ejecutar()
            elif opcion == "3":
                self.gestor.agregar.ejecutar()
            elif opcion == "4":
                self.gestor.modificar.ejecutar()
            elif opcion == "5":
                self.gestor.borrar.ejecutar()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
