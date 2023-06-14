from clasetestautomatiado import TestAutomatizado
if __name__=='__main__':
  lista_vehiculos = ListaVehiculos()
  vehiculo1 = Vehiculo("ABC123", "Toyota", "Corolla", 2018, 15000)
  vehiculo2 = Vehiculo("DEF456", "Honda", "Civic", 2019, 18000)
  vehiculo3 = Vehiculo("GHI789", "Ford", "Focus", 2020, 20000)
  lista_vehiculos.agregarElemento(vehiculo1)
  lista_vehiculos.agregarElemento(vehiculo2)
  lista_vehiculos.agregarElemento(vehiculo3)
  
  # Crear una instancia de la clase de pruebas automatizadas
  test = TestAutomatizado(lista_vehiculos)
  
  # Ejecutar los tests
  test.test_insertar_vehiculo(Vehiculo("JKL012", "Chevrolet", "Cruze", 2017, 14000), 0)
  test.test_insertar_vehiculo(Vehiculo("MNO345", "Volkswagen", "Golf", 2016, 12000), 2)
  test.test_insertar_vehiculo(Vehiculo("PQR678", "Hyundai", "Elantra", 2015, 11000), -1)
  
  test.test_agregar_vehiculo(Vehiculo("STU901", "Kia", "Sorento", 2021, 25000))
  
  test.test_obtener_objeto(2)
  
  test.test_modificar_precio_venta("ABC123", 16000)