class Bus:
    def __init__(self, capacidad_total, pasajeros_actuales):
        self.capacidad_total = capacidad_total
        self.pasajeros_actuales = pasajeros_actuales

    # a) Subir pasajeros y actualizar datos
    def subir_pasajeros(self, cantidad):
        asientos_disponibles = self.capacidad_total - self.pasajeros_actuales
        
        if cantidad <= asientos_disponibles:
            self.pasajeros_actuales = self.pasajeros_actuales + cantidad
            print("Subieron", cantidad, "pasajeros con éxito.")
        else:
            print("Error: No hay espacio suficiente para que suban", cantidad, "pasajeros.")

    # b) Cobrar pasaje a los pasajeros (Costo: bs. 1.50)
    def cobrar_pasaje(self):
        costo_pasaje = 1.50
        total_recaudado = self.pasajeros_actuales * costo_pasaje
        print("Total cobrado a los", self.pasajeros_actuales, "pasajeros: Bs.", total_recaudado)

    # c) Muestra cuántos asientos quedan disponibles
    def mostrar_asientos_disponibles(self):
        disponibles = self.capacidad_total - self.pasajeros_actuales
        print("Asientos disponibles:", disponibles)


# d) Crea una instancia del bus y utiliza los métodos de los incisos anteriores

# Bus con capacidad para 30 personas y 10 pasajeros iniciales
mi_bus = Bus(30, 10)

print("--- ESTADO INICIAL ---")
mi_bus.mostrar_asientos_disponibles()

print("\n--- SUBIENDO PASAJEROS ---")
mi_bus.subir_pasajeros(5)  # Suben 5
mi_bus.mostrar_asientos_disponibles()

print("\n--- COBRANDO PASAJES ---")
mi_bus.cobrar_pasaje()

print("\n--- INTENTO DE SUBIR MÁS PASAJEROS DE LA CAPACIDAD ---")
mi_bus.subir_pasajeros(20)  # Intentan subir 20 (solo quedan 15 asientos)
