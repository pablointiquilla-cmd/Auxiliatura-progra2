class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    # a) y c) Método depositar con validación
    def depositar(self, monto):
        if monto <= 0:
            print("Error: El monto a depositar debe ser mayor a 0.")
        else:
            self.saldo = self.saldo + monto
            print("Depósito realizado con éxito. Nuevo saldo:", self.saldo)

    # a) y b) Método retirar con validación
    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: Saldo insuficiente. No se puede retirar ese monto.")
        elif monto <= 0:
            print("Error: El monto a retirar debe ser mayor a 0.")
        else:
            self.saldo = self.saldo - monto
            print("Retiro realizado con éxito. Nuevo saldo:", self.saldo)

    # d) Mostrar los datos de la cuenta
    def mostrar_datos(self):
        print("Titular:", self.titular)
        print("Número de cuenta:", self.nroCuenta)
        print("Saldo disponible:", self.saldo)


# --- PROGRAMA PRINCIPAL ---

# Crear el objeto de la cuenta bancaria
mi_cuenta = CuentaBancaria("Carlos Mamani", 10020304, 500)

print("--- DATOS INICIALES ---")
mi_cuenta.mostrar_datos()

print("\n--- PRUEBA DE DEPOSITOS ---")
# Depósito válido
mi_cuenta.depositar(200)

# c) Intento de depósito inválido (negativo y cero)
mi_cuenta.depositar(-50)
mi_cuenta.depositar(0)

print("\n--- PRUEBA DE RETIROS ---")
# Retiro válido
mi_cuenta.retirar(100)

# b) Intento de retiro superior al saldo
mi_cuenta.retirar(1000)

print("\n--- DATOS FINALES ---")
mi_cuenta.mostrar_datos()
