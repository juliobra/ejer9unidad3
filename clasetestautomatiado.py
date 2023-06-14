class TestAutomatizado:

    def __init__(self, lista_vehiculos):
        self.lista_vehiculos = lista_vehiculos

    def test_insertar_vehiculo(self, vehiculo, posicion):
        print("Estado inicial de la lista:", self.lista_vehiculos)
        self.lista_vehiculos.insertarElemento(vehiculo, posicion)
        print("Estado final de la lista:", self.lista_vehiculos)

    def test_agregar_vehiculo(self, vehiculo):
        print("Estado inicial de la lista:", self.lista_vehiculos)
        self.lista_vehiculos.agregarElemento(vehiculo)
        print("Estado final de la lista:", self.lista_vehiculos)

    def test_obtener_objeto(self, posicion):
        objeto = self.lista_vehiculos.mostrarElemento(posicion)
        print("Objeto obtenido:", objeto)

    def test_modificar_precio_venta(self, patente, nuevo_precio_venta):
        vehiculo = self.lista_vehiculos.buscarVehiculo(patente)
        if vehiculo is not None:
            print("Precio de venta anterior:", vehiculo.precio_venta)
            vehiculo.modificarPrecioVenta(nuevo_precio_venta)
            print("Nuevo precio de venta:", vehiculo.precio_venta)
        else:
            print("Vehículo no encontrado")