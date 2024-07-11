class Vehiculo:
    def __init__(self) -> None:
        self.marca = ''
        self.modelo = ''
        self.ano = ''
        self. lista_vehiculo = []
        self.prender_luces = False
    
    def agregar_vehiculo(self):
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        ano = input("Ingrese el año del vehículo: ")
        self.lista_vehiculo.append({'marca': marca, 'modelo': modelo, 'ano': ano})
        print("Vehículo agregado correctamente.")
    
    def mostrar_vehiculo(self):
        for vehiculo in self.lista_vehiculo:
            print(f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Año: {vehiculo['ano']}")
        print("Todos los vehículos han sido mostrados.")
    
    def buscar_vehiculo(self):
        marca = input("Ingrese la marca del vehículo a buscar: ")
        for vehiculo in self.lista_vehiculo:
            if vehiculo['marca'] == marca:
                print(f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Año: {vehiculo['ano']}")
            else:
                print("No se encontró el vehículo.")
    
    def montarse_vehiculo(self):
        if self.lista_vehiculo:
            print(f"{self.lista_vehiculo} está montado.")
        else:
            print("No hay vehículos para montar.")                
    
    def correr(self, velocidad):
        if velocidad > 0:
            print(f"{self.lista_vehiculo} está corriendo a {velocidad} km/h.")
        else:
            print("El vehículo no puede correr a una velocidad no positiva.")

    def frenar(self, velocidad):
        if velocidad >= 0:
            print(f"{self.lista_vehiculo} está frenando a {velocidad} km/h.")
        else:
            print("El vehículo no puede frenar desde una velocidad negativa.")

    def encender(self, llave_insertada):
        if llave_insertada:
            print(f"{self.lista_vehiculo} está encendido.")
        else:
            print("Inserta la llave para encender el vehículo.")

    def prender_luces(self, encender):
        if encender == self.lista_vehiculo or encender:
            print(f"tiene las luces {encender}.")

    def acelerar(self, velocidad_actual, aceleracion):
        if velocidad_actual >= 0:
            nueva_velocidad = velocidad_actual + aceleracion
            print(f"{self.lista_vehiculo} está acelerando a {nueva_velocidad} km/h.")
        else:
            print("El vehículo no puede acelerar desde una velocidad negativa.")

    def abrir_puerta(self, llave_insertada):
        if llave_insertada:
            print(f"{self.lista_vehiculo} ha abierto la puerta.")
        else:
            print("Inserta la llave para abrir la puerta.")

    def montarse(self, pasajero):
        if pasajero:
            print(f"{self.lista_vehiculo} se ha montado en el vehículo.")
        else:
            print("No hay pasajero para montarse.")

    def dar_marcha_atras(self, marcha_atras_activada):
        if marcha_atras_activada:
            print(f"{self.lista_vehiculo} está en marcha atrás.")
        elif self.lista_vehiculo is not None: 
            print(f"{self.lista_vehiculo} está en marcha atrás.")
        else:
            print("La marcha atrás está desactivada.")

    def estacionarse(self, espacio_libre):
        if espacio_libre:
            print(f"{self.lista_vehiculo} está estacionado.")
        else:
            print("No hay suficiente espacio para estacionarse aquí.")
            
vehiculo = Vehiculo()
def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Vehículo")
        print("2. Mostrar Vehículos")
        print("3. Buscar Vehículo")
        print("4. Abrir Puerta Vehículo")
        print("5. montarse_vehiculo")
        print("6. Encender Vehículo")
        print("7. Prender Luces Vehículo")
        print("8. Correr Vehículo")
        print("9. Acelerar Vehículo")
        print("10. Frenar Vehículo")
        print("11. Montar Pasajero Vehículo")
        print("12. Dar Marcha Atrás Vehículo")
        print("13. Estacionar Vehículo")
        print("14. Salir")
    
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            vehiculo.agregar_vehiculo()
            
        elif opcion == 2:
            vehiculo.mostrar_vehiculo()
            
        elif opcion == 3:
            vehiculo.buscar_vehiculo()
            
        elif opcion == 4:
            llave_insertada = bool(input("¿Tiene la llave insertada? (S/N): ").lower() == 's')
            vehiculo.abrir_puerta(llave_insertada)
            
        elif opcion == 5:
            vehiculo.montarse_vehiculo()    
            
        elif opcion == 6:
            llave_insertada = bool(input("¿Tiene la llave insertada? (S/N): ").lower() =='s')
            vehiculo.encender(llave_insertada)
        
        elif opcion == 7:
            encender = bool(input("¿Quiere encender las luces? (S/N): ").lower() == 's')
            vehiculo.prender_luces(encender)
            
        elif opcion == 8:
            velocidad = int(input("Ingrese la velocidad a correr (en km/h): "))
            vehiculo.correr(velocidad)
            
        elif opcion ==9:
            velocidad_actual = int(input("Ingrese la velocidad actual (en km/h): "))
            aceleracion = int(input("Ingrese la aceleración (en km/h²): "))
            vehiculo.acelerar(velocidad_actual, aceleracion)
            vehiculo.correr(velocidad_actual + aceleracion)
            
        elif opcion == 10:
            velocidad = int(input("Ingrese la velocidad a frenar (en km/h): "))
            vehiculo.frenar(velocidad)

        elif opcion == 11:
            pasajero = bool(input("¿Tiene pasajero? (S/N): ").lower() == 's')
            vehiculo.montarse(pasajero)
            if pasajero:
                vehiculo.llevar_pasajeros()
                
        elif opcion == 12:
            marcha_atras_activada = bool(input("¿Activa la marcha atrás? (S/N): ").lower() == 's')
            vehiculo.dar_marcha_atras(marcha_atras_activada)
            if marcha_atras_activada:
                vehiculo.correr(0)
                
        elif opcion == 13:
            espacio_libre = bool(input("¿Hay espacio libre para estacionarse? (S/N): ").lower() == 's')
            vehiculo.estacionarse(espacio_libre)

        elif opcion == 14:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    menu()
