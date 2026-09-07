class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")
        print("Almacenamiento:", self.almacenamiento, "GB")

    # b) Determinar si la cantidad de memoria RAM es igual a X
    def comparar_ram(self, x):
        if self.ram == x:
            print("La RAM de la computadora es igual a", x, "GB")
        else:
            print("La RAM de la computadora NO es igual a", x, "GB")

# a) Instanciar 2 objetos de diferente forma

# Forma 1: Asignando los valores directamente en el constructor
compu1 = Computadora("HP", "Intel i5", 8, 512)

# Forma 2: Pidiendo los datos al usuario por teclado
print("--- Ingrese los datos de la segunda computadora ---")
marca2 = input("Marca: ")
procesador2 = input("Procesador: ")
ram2 = int(input("RAM (GB): "))
almacenamiento2 = int(input("Almacenamiento (GB): "))

compu2 = Computadora(marca2, procesador2, ram2, almacenamiento2)

print("\n----------------------------------")

# b) Determinar si la cantidad de memoria RAM es igual a X (ejemplo con X = 8)
X = 8
print("Verificando si compu1 tiene", X, "GB de RAM:")
compu1.comparar_ram(X)

print("\n----------------------------------")

# c) De 2 computadoras, mostrar los datos de la que tiene mayor capacidad de almacenamiento
print("Computadora con mayor almacenamiento:")
if compu1.almacenamiento > compu2.almacenamiento:
    compu1.mostrar_datos()
elif compu2.almacenamiento > compu1.almacenamiento:
    compu2.mostrar_datos()
else:
    print("Ambas computadoras tienen el mismo almacenamiento:")
    compu1.mostrar_datos()
