""" Clase base: CuentaBancaria """
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Realiza un depósito en la cuenta"""
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad de depósito no válida.")

    def retirar(self, cantidad):
        """Realiza un retiro de la cuenta"""
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente o cantidad no válida.")

    def consultar_saldo(self):
        """Consulta el saldo actual de la cuenta"""
        return f"Saldo actual de {self.titular}: {self.saldo}"

    def generar_reporte(self):
        """Genera un reporte de la cuenta"""
        return f"Cuenta de {self.titular} - Saldo: {self.saldo}"

"""
Subclase: CuentaDeAhorros
"""
class CuentaDeAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.02):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        """Aplica el interés al saldo de la cuenta de ahorros"""
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        print(f"Interés aplicado. Nuevo saldo: {self.saldo}")

    def generar_reporte(self):
        """Genera un reporte de la cuenta con interés aplicado"""
        reporte_base = super().generar_reporte()
        return f"{reporte_base} - Tasa de interés: {self.tasa_interes * 100}%"

"""
Función para crear una cuenta bancaria
"""

def crear_cuenta():
    print("Bienvenido al sistema de gestión de cuentas bancarias")
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    
    cuenta_tipo = input("¿Desea crear una cuenta de ahorro? (sí/no): ").lower()
    if cuenta_tipo == "sí":
        tasa_interes = float(input("Ingrese la tasa de interés (por ejemplo, 0.02 para 2%): "))
        cuenta = CuentaDeAhorros(titular, saldo_inicial, tasa_interes)
    else:
        cuenta = CuentaBancaria(titular, saldo_inicial)
    
    return cuenta

"""
 Función para gestionar las operaciones
"""
 
def menu_principal(cuenta):
    while True:
        print("\n¿Qué operación desea realizar?")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Aplicar interés (solo cuentas de ahorro)")
        print("5. Generar reporte")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            print(cuenta.consultar_saldo())
        elif opcion == "4" and isinstance(cuenta, CuentaDeAhorros):
            cuenta.aplicar_interes()
        elif opcion == "5":
            print(cuenta.generar_reporte())
        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida o no disponible para este tipo de cuenta.")
            
cuenta = crear_cuenta()
menu_principal(cuenta)

