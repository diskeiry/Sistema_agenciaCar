import time

class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.encendido = False
        self.puerta_abierta = False
        self.luces_encendidas = False
        self.velocidad = 0
        
      
    def abrir_puerta(self, llave_insertada):
        if llave_insertada:
            self.puerta_abierta = True
            print(f"{self.marca} {self.modelo} del el año: {self.ano} ha abierto la puerta.")
        else:
            print("Inserta la llave para abrir la puerta.")
      
    def montarse_vehiculo(self):
        if not self.puerta_abierta:
            print("No hay llaves para abrir puerta de el vehículo.")
        else:
            print(f"Te has montado en el vehículo: {self.marca} {self.modelo} del el año: {self.ano}")
    
   
    def encender_vehiculo(self):
        if not self.montarse_vehiculo:
            print("No Tienes la llave para encender el vehículo.")
            return False
        elif not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo}: Vehículo encendido.")
        else:
            print(f"{self.marca} {self.modelo}: El vehículo ya está encendido.")
            
    def prender_luces(self):
        if not self.encender_vehiculo and not self.luces_encendidas:
            self.luces_encendidas = True
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: Luces encendidas.")
        elif not self.encendido:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se pueden encender las luces, el vehículo está apagado.")
        else:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: Las luces ya están encendidas.")
        
    def apagar_luces(self):
        if self.luces_encendidas:
            self.luces_encendidas = False
            print(f"{self.marca} {self.modelo}: Luces apagadas.")
        elif not self.luces_encendidas:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se pueden apagar las luces, La luz estan apagada.")
        else:
            print(f"{self.marca} {self.modelo}: Las luces ya están apagadas.")
    
    def corriendo(self, cantidad):
        if self.encendido:
            self.velocidad += cantidad
            print(f"{self.marca} {self.modelo}: Corriendo a {self.velocidad} km/h.")
        else:
            print(f"{self.marca} {self.modelo}: No se puede acelerar, el vehículo está apagado.")       
            
    def acelerar(self, aceleracion):
        if self.encendido == 0:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede acelerar, el vehículo está apagado.")
            return False
        elif self.velocidad + aceleracion > 0:
            self.velocidad += aceleracion
            print(f"{self.marca} {self.modelo} del el año: {self.ano} está acelerando a {self.velocidad} km/h.")
        else:
            print("El vehículo no puede acelerar a una velocidad negativa.")
            
    def frenar(self, cantidad):
        if self.encendido == 0:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede frenar, el vehículo está apagado.")
            return False
        elif self.encendido:
            if self.velocidad - cantidad >= 1:
                self.velocidad -= cantidad
                print(f"{self.marca} {self.modelo} del el año: {self.ano}: corriendo a {self.velocidad} km/h.")
            else:
                self.velocidad = 0
                print(f"{self.marca} {self.modelo} del el año: {self.ano}: Vehículo detenido.")
        else:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede frenar, el vehículo está apagado.")
            
    def dar_marcha_atras(self, marcha_atras_activada):
        if self.encendido == 0:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede dar marcha atras, el vehículo está apagado.")
            return False
        elif self.velocidad == 0:
            self.frenar = marcha_atras_activada
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: Dando marcha atras")
        else:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede dar marcha atras, la velocidad es a: {self.velocidad} km/h Tiene que frenar para activar marcha atras.")
             

    def estacionarse(self, espacio_libre):
        if self.encendido == 0:
            print(f"{self.marca} {self.modelo} del el año: {self.ano}: No se puede estacionar, el vehículo está apagado.")
            return False
        elif self.velocidad > 0:
            print(f"{self.marca} {self.modelo} del el año: {self.ano} no puede estacionarse, la velocidad es a: {self.velocidad} km/h Tiene que frenar para estacionarse.")
               
        elif espacio_libre:
            print(f"{self.marca} {self.modelo} del el año: {self.ano} está estacionado.")
        else:
            print("No hay suficiente espacio para estacionarse aquí.")
        

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = 0
        
    def cargar(self, hierro):
        self.carga_maxima += hierro
        print(f"{self.marca} {self.modelo} del el año: {self.ano} está cargando hasta {self.carga_maxima} kg.")
        

     
    def remolcar(self, hierro):
       if self.carga_maxima - hierro >= 0:
            self.carga_maxima -= hierro
            print(f"{self.marca} {self.modelo} del el año: {self.ano} está remolcando hasta {self.carga_maxima} kg.")
       else:
            print(f"{self.marca} {self.modelo} del el año: {self.ano} no tiene suficiente carga para remolcar.")
       



class Camion(Vehiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.carga = 0

    def cargar(self, peso):
        self.carga += peso
        print(f"{self.marca} {self.modelo}: Cargando {peso} kg. Carga total: {self.carga} kg.")

    def descargar(self, peso):
        if self.carga - peso >= 0:
            self.carga -= peso
            print(f"{self.marca} {self.modelo}: Descargando {peso} kg. Carga total: {self.carga} kg.")
        else:
            print(f"{self.marca} {self.modelo}: No se puede descargar más de lo que está cargado.")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.pasajeros = 0

    def llevar_pasajeros(self, persona):
        if self.pasajeros + persona >= 7:
            self.pasajeros += persona
            print(f"{self.marca} {self.modelo} {self.ano} ha llevado {persona} pasajeros.")
        else:
            print(f"{self.marca} {self.modelo} {self.ano} no puede llevar más de 7 pasajeros.")
        
            
    def demontar_pasajeros(self, persona):
        if self.pasajeros - persona >= 0:
            self.pasajeros -= persona
            print(f"{self.marca} {self.modelo} {self.ano} ha desmontado {persona} pasajeros.")
        else:
            print(f"{self.marca} {self.modelo} {self.ano} no puede desmontar porque no hay {self.pasajeros} pasajeros.")
        


class Motor(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible, ano):
        super().__init__(marca, modelo, ano)
        self.burro_colocado = False
        
    def colocar_burro(self):
        if not self.burro_colocado:
            self.burro_colocado = True
            print(f"{self.marca} {self.modelo}: Burro colocado.")
        else:
            print(f"{self.marca} {self.modelo}: El burro ya está colocado.")

    def quitar_burro(self):
        if self.burro_colocado:
            self.burro_colocado = False
            print(f"{self.marca} {self.modelo}: Burro quitado.")
        else:
            print(f"{self.marca} {self.modelo}: El burro ya está quitado.")

# Instanciando objetos de las clases Vehiculo, Camioneta, Camión, Carro y Motor

# Menú para acceder a los vehículos y sus métodos
def menu():
    print("\nMenú de vehículos:")
    print("1. Camioneta")
    print("2. Camión")
    print("3. Carro")
    print("4. Motor")
    print("5. salir")
    

# Menú para acceder a los métodos de los vehículos
    
    
def mostrar_menu_vehiculo():
    print("\nMenu Principal:")
    print("1. Abrir Puerta Vehículo")
    print("2. montarse vehiculo")
    print("3. Encender Vehículo")
    print("4. Prender Luces Vehículo")
    print("5. apagar Luces Vehiculo")
    print("6. corriendo Vehículo")
    print("7. Acelerar Vehículo")
    print("8. Frenar Vehículo")
    print("9. Dar Marcha Atrás Vehículo")
    print("10. Estacionar Vehículo")
    print("11. Acción especial")
    print("12. Volver al menu principal")
          

# Programa principal
if __name__ =="__main__":
    Vehiculo = {
       1: Camioneta( "Toyota", "Hilux", 2024),
       2: Camion("Chevrolet", "Spark", 2020),
       3: Carro("Ford", "Mustang", 2021),
       4: Motor("Honda", "Civic", "gasolina", 2022)
    }                    
 
    while True:
        menu()
        accion = int(input("Introduce el número de tu opción: "))

        if accion == 5:
            print("SALIENDO DEL SISTEMA...")
            break

        if accion in Vehiculo:
            vehiculo = Vehiculo[accion]
            while True:
                mostrar_menu_vehiculo()
                accion = int(input("Introduce el número de tu opción: "))
                
                if accion == 1:
                    llave_insertada = bool(input("¿Tiene la llave insertada? (S/N): ").lower() == 's')
                    vehiculo.abrir_puerta(llave_insertada)
                elif accion == 2:
                    vehiculo.montarse_vehiculo()
                    
                elif accion == 3:
                    vehiculo.encender_vehiculo()
                    
                elif accion == 4:
                    vehiculo.prender_luces()
                    
                elif accion == 5:
                    vehiculo.apagar_luces()
                    
                elif accion == 6:
                    cantidad = int(input("¿Cuánto quieres correr (km/h)? "))
                    vehiculo.corriendo(cantidad)
                    
                elif accion ==7:
                    cantidad = int(input("¿Cuánto quieres acelerar (km/h)? "))
                    for i in range(cantidad):
                        i =+(i+1 if i == 0 else i + 1)
                        print(f"\rVelocidad acelerada es: {i} ",end='', flush=True)
                        time.sleep(000.1)
                    vehiculo.acelerar(cantidad)
                 
                elif accion == 8:
                    cantidad = int(input("¿Cuánto quieres frenar (km/h)? "))
                    for i in range(cantidad, -1, -1):
                        print(f"\rVelocidad desacelerando es: {i} ",end='', flush=True)
                        time.sleep(000.1)
                    vehiculo.frenar(cantidad)
                    
                elif accion == 9:
                    marcha_atras_activada = bool(input("¿Activa la marcha atrás? (S/N): ").lower() == 's')
                    vehiculo.dar_marcha_atras(marcha_atras_activada)
                        
                elif accion == 10:
                    espacio_libre = bool(input("¿Hay espacio libre para estacionarse? (S/N): ").lower() == 's')
                    vehiculo.estacionarse(espacio_libre)
                
                elif accion == 11:
                    if isinstance(vehiculo, Camioneta):
                        subAccion = input("¿Remolcar o cargar? ")
                        if subAccion.lower() == "remolcar":
                            hierro = int(input("Introduce el peso (kg): "))
                            vehiculo.remolcar(hierro)
                        elif subAccion.lower() == "cargar":
                            vehiculo.cargar(hierro)
                            
                    if isinstance(vehiculo, Camion):
                        subaccion = input("¿Cargar o descargar? ")
                        peso = int(input("Introduce el peso (kg): "))
                        if subaccion.lower() == "cargar":
                            vehiculo.cargar(peso)
                        elif subaccion.lower() == "descargar":
                            vehiculo.descargar(peso)
                            
                    elif isinstance(vehiculo, Carro):
                        subAccion = bool(input("¿Tiene pasajero? (S/N): ").lower() == 's')
                        persona = int(input("Introduce cantidad de persona: "))
                        vehiculo.llevar_pasajeros(persona)
                        persona = int(input("Introduce cantidad de persona para demontar: "))
                        vehiculo.demontar_pasajeros(persona)
                            
                    elif isinstance(vehiculo, Motor):
                        subAccion = input("¿Colocar o quitar burro? ")
                        if subAccion.lower() == "colocar":
                            vehiculo.colocar_burro()
                        elif subAccion.lower() == "quitar":
                            vehiculo.quitar_burro()
                    
                elif accion == 12:
            
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        menu()
