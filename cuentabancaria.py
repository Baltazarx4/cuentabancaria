class CuentaBancaria:
    def __init__(self, balance=0, tasa_interes=0.01):
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito(self, monto):
        if monto > 0:
            self.balance += monto
        return self

    def retiro(self, monto):
        if monto > 0 and self.balance >= monto:
            self.balance -= monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

# Ejemplo
cuenta = CuentaBancaria(1000, 0.02)

cuenta.deposito(500).retiro(200).mostrar_info_cuenta().generar_interes().mostrar_info_cuenta()
