class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self._numero_conta = numero_conta  # Atributo privado
        self._saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("Saldo insuficiente.")

    def _exibir_saldo(self):  # Método privado
        print(f"Saldo: R${self._saldo:.2f}")


conta1 = ContaBancaria("1234", 1000)
conta1.depositar(500)
conta1.sacar(200)
conta1._exibir_saldo()  # Acesso ao método privado
