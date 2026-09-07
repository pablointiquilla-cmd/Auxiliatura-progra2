class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje, color="Sin color"):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = color

    # a) Método para mostrar el kilometraje en kilómetros y metros
    def mostrar_kilometraje(self):
        km = self.kilometraje
        metros = self.kilometraje * 1000
        print("Kilometraje en kilómetros:", km, "km")
        print("Kilometraje en metros:", metros, "m")

    # b) Método para cambiar el color del auto
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print("El nuevo color del vehículo es:", self.color)

    # Método extra básico para ver la información del auto
    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)
        print("Color:", self.color)


# c) Crea dos autos, cámbiales el color y muestra su kilometraje en kilómetros y metros.

print("--- AUTO 1 ---")
auto1 = Vehiculo("Toyota", "Corolla", 2018, 50, "Blanco")
auto1.mostrar_info()

print("\nCambiando color al auto 1:")
auto1.cambiar_color("Rojo")

print("\nKilometraje del auto 1:")
auto1.mostrar_kilometraje()

print("\n--------------------")

print("\n--- AUTO 2 ---")
auto2 = Vehiculo("Nissan", "Sentra", 2020, 120, "Gris")
auto2.mostrar_info()

print("\nCambiando color al auto 2:")
auto2.cambiar_color("Negro")

print("\nKilometraje del auto 2:")
auto2.mostrar_kilometraje()
